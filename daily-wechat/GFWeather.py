import os
import time
from datetime import datetime

import itchat
import requests
import yaml
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import city_dict

load_dotenv()

sckey = os.getenv('SCKEY', None)

if not sckey:
    raise ValueError()

# fire the job again if it was missed within GRACE_PERIOD
GRACE_PERIOD = 15 * 60


class GFWeather:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    dictum_channel_name = {1: 'ONE●一个', 2: '词霸(每日英语)'}

    def __init__(self):
        self.friend_list, self.alarm_hour, self.alarm_minute, self.dictum_channel = self.get_init_data()

    def get_init_data(self):
        """
        初始化基础数据
        :return: None
        """
        with open('_config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.Loader)

        alarm_timed = config.get('alarm_timed').strip()
        init_msg = f"每天定时发送时间：{alarm_timed}\n"

        dictum_channel = config.get('dictum_channel', -1)
        init_msg += f"格言获取渠道：{self.dictum_channel_name.get(dictum_channel, '无')}\n"

        friend_list = []
        friend_infos = config.get('friend_infos')

        for friend in friend_infos:
            friend.get('wechat_name').strip()
            # 根据城市名称获取城市编号，用于查询天气。查看支持的城市为：http://cdn.sojson.com/_city.json
            city_name = friend.get('city_name').strip()
            city_code = city_dict.city_dict.get(city_name)
            if not city_code:
                print('您输入的城市无法收取到天气信息')
                break
            friend['city_code'] = city_code
            friend_list.append(friend)

            print_msg = f"朋友的微信昵称：{friend.get('wechat_name')}\n\t朋友所在城市名称：{friend.get('city_name')}\n\t" \
                f"成功运行的第一天日期：{friend.get('start_date')}\n\t最后一句为：{friend.get('sweet_words')}\n"
            init_msg += print_msg

        print(u"*" * 50)
        print(init_msg)

        hour, minute = [int(x) for x in alarm_timed.split(':')]
        return friend_list, hour, minute, dictum_channel

    def is_online(self, auto_login=False):
        """
        判断是否还在线,
        :param auto_login: bool,如果掉线了则自动登录(默认为 False)。
        :return: bool,当返回为 True 时，在线；False 已断开连接。
        """

        def online():
            """
            通过获取好友信息，判断用户是否还在线
            :return: bool,当返回为 True 时，在线；False 已断开连接。
            """
            try:
                if itchat.search_friends():
                    return True
            except:
                desp = F'{datetime.now().strftime("%Y-%m-%d %H:%M")}\n微信已掉线'
                self.server_chan(desp)
                return False
            return True

        if online():
            return True
        # 仅仅判断是否在线 执行到这一步说明 online 是 False
        if not auto_login:
            return False

        # 登陆，尝试 5 次
        for _ in range(5):
            # 命令行显示登录二维码
            itchat.auto_login(hotReload=True, enableCmdQR=2)
            if online():
                print('登录成功')
                return True
        else:
            print('登录成功')
            return False

    def server_chan(self, desp):
        """server酱推送信息至微信"""
        url = F'https://sc.ftqq.com/{sckey}.send'

        data = {
            'text': 'daily-wechat',
            'desp': desp,
        }
        res = requests.post(url, data=data)
        return True if res.status_code == 200 else False

    def run(self):
        """
        主运行入口
        :return:None
        """
        # 自动登录
        if not self.is_online(auto_login=True):
            return
        for friend in self.friend_list:
            friend_type = friend.get('type')
            wechat_name = friend.get('wechat_name')
            if friend_type == 'person':
                friends = itchat.search_friends(name=wechat_name)
            elif friend_type == 'group':
                friends = itchat.search_chatrooms(name=wechat_name)
            else:
                print('配置文件 type 类型指定错误')
                continue
            if not friends:
                print('昵称有误')
                return
            friend['uin'] = friends[0].get('UserName')

        # 定时任务
        scheduler = BlockingScheduler()
        scheduler.add_job(self.start_today_info, 'cron', hour=self.alarm_hour,
                          minute=self.alarm_minute, misfire_grace_time=GRACE_PERIOD,
                          max_instances=len(self.friend_list))
        # scheduler.add_job(self.start_today_info, 'interval', seconds=10, max_instances=len(self.friend_list))
        # 心跳包检测 每 5 分钟 后续加入 掉线通知 使用了 server 酱
        scheduler.add_job(self.is_online, 'interval', minutes=5, kwargs={'auto_login': True})
        scheduler.start()

    def start_today_info(self, is_test=False):
        """
        每日定时开始处理。
        :param is_test:bool, 测试标志，当为True时，不发送微信信息，仅仅获取数据。
        :return: None。
        """
        print("*" * 50)
        print('获取相关信息...')

        if self.dictum_channel == 1:
            dictum_msg = self.get_dictum_info()
        elif self.dictum_channel == 2:
            dictum_msg = self.get_ciba_info()
        else:
            dictum_msg = ''

        for friend in self.friend_list:
            city_code = friend.get('city_code')
            start_date = friend.get('start_date').strip()
            sweet_words = friend.get('sweet_words')
            uin = friend.get('uin')
            today_msg = self.get_weather_info(dictum_msg, city_code=city_code, start_date=start_date,
                                              sweet_words=sweet_words)
            wechat_name = friend.get('wechat_name')
            # 后续 print 改为 logger 日志
            # print(f'给『{wechat_name}』发送的内容是:\n{today_msg}')

            if not is_test:
                if self.is_online(auto_login=True):
                    itchat.send(today_msg, toUserName=uin)

                # 防止信息发送过快。
                time.sleep(5)

        # 推送成功
        desp = F'{datetime.now().strftime("%Y-%m-%d %H:%M")}\n 每日推送成功'
        self.server_chan(desp)

    def isJson(self, resp):
        """
        判断数据是否能被 Json 化。 True 能，False 否。
        :param resp: request
        :return: bool, True 数据可 Json 化；False 不能 JOSN 化。
        """
        try:
            resp.json()
            return True
        except:
            return False

    def get_ciba_info(self):
        """
        从词霸中获取每日一句，带英文。
        :return:str ,返回每日一句（双语）
        """
        print('获取格言信息（双语）...')
        resp = requests.get('http://open.iciba.com/dsapi')
        if resp.status_code == 200 and self.isJson(resp):
            conentJson = resp.json()
            content = conentJson.get('content')
            note = conentJson.get('note')
            return f"{content}\n{note}\n"
        else:
            print("没有获取到数据")
            return None

    def get_dictum_info(self):
        """
        获取格言信息（从『一个。one』获取信息 http://wufazhuce.com/）
        :return: str， 一句格言或者短语
        """
        print('获取格言信息...')
        user_url = 'http://wufazhuce.com/'
        resp = requests.get(user_url, headers=self.headers)
        if resp.status_code == 200:
            soup_texts = BeautifulSoup(resp.text, 'lxml')
            # 『one -个』 中的每日一句
            every_msg = soup_texts.find_all('div', class_='fp-one-cita')[0].find('a').text
            return every_msg + "\n"
        print('每日一句获取失败')
        return ''

    def get_weather_info(self, dictum_msg='', city_code='101030100', start_date='2018-01-01',
                         sweet_words='From your Valentine'):
        """
        获取天气信息。网址：https://www.sojson.com/blog/305.html
        :param dictum_msg: str,发送给朋友的信息
        :param city_code: str,城市对应编码
        :param start_date: str,恋爱第一天日期
        :param sweet_words: str,来自谁的留言
        :return: str,需要发送的话。
        """
        print('获取天气信息...')
        weather_url = f'http://t.weather.sojson.com/api/weather/city/{city_code}'
        resp = requests.get(url=weather_url)
        if resp.status_code == 200 and self.isJson(resp) and resp.json().get('status') == 200:
            weatherJson = resp.json()
            # 今日天气
            today_weather = weatherJson.get('data').get('forecast')[0]
            # 今日日期
            today_time = datetime.now().strftime('%Y{y}%m{m}%d{d} %H:%M:%S').format(y='年', m='月', d='日')
            # 今日天气注意事项
            notice = today_weather.get('notice')
            # 温度
            high = today_weather.get('high')
            high_c = high[high.find(' ') + 1:]
            low = today_weather.get('low')
            low_c = low[low.find(' ') + 1:]
            temperature = f"温度 : {low_c}/{high_c}"

            # 风
            fx = today_weather.get('fx')
            fl = today_weather.get('fl')
            wind = f"{fx} : {fl}"

            # 空气指数
            aqi = today_weather.get('aqi')
            aqi = f"空气 : {aqi}"

            # 成功运行的天数
            if start_date:
                try:
                    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
                    # 如果不 +1 如果是当天 会显示 0
                    day_delta = (datetime.now() - start_datetime).days + 1
                    delta_msg = f'一如既往成功运行的第 {day_delta} 天。\n'
                except:
                    delta_msg = ''
            else:
                delta_msg = ''

            today_msg = f'{today_time}\n{delta_msg}{notice}。\n{temperature}\n{wind}\n{aqi}\n{dictum_msg}{sweet_words if sweet_words else ""}\n'
            return today_msg


if __name__ == '__main__':
    # 只查看获取数据，
    # GFWeather().start_today_info(True)

    # 测试获取词霸信息
    # ciba = GFWeather().get_ciba_info()
    # print(ciba)

    # 测试获取每日一句信息
    # dictum = GFWeather().get_dictum_info()
    # print(dictum)

    # 测试获取天气信息
    # wi = GFWeather().get_weather_info('sorry \n')
    # print(wi)
    pass
