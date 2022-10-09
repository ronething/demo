# coding=utf-8

import jieba
import json
import re
from collections import Counter

out_jieba = '../jieba.json'


def jieba_custom():
    custom_word_list = ['树莓派','公众号','哔哩哔哩','百度网盘','红黑联盟','吾爱破解','以太坊','前后端',
                        '中州韻輸入法引擎','再创世纪']
    for i in custom_word_list:
        jieba.add_word(i)
    # jieba.suggest_freq('树莓派',True)

def cut_json(data):
    jieba_custom()
    filter_str = r'\s+|–|-|_|\||\.|,|，|、|—|:|：|\/|的|）|（|\(|\)|和|吧|&|!|【|】|\？|\'|゜|\[|\]|与|让|用|·|•|»|=|\+|~|在|不|《|》|你|！|之|及|是|\?|上|下|到|。|\…|「|」|“|”|#|『|』|๑'
    space_regex = re.compile(filter_str)
    for bookmark in data:
        name = space_regex.sub(r'', bookmark['name'])
        yield from jieba.cut(name, cut_all=False)


def main():
    with open('../bookmark.json', 'r', encoding='utf-8') as f:
        contents = json.load(f)

    res = cut_json(contents['data'])
    
    # 取出 top 300
    top = 300
    jieba_list = Counter(list(res)).most_common(top)
    # print(dict(jieba_list))


    with open(out_jieba,'w+',encoding='utf-8') as f:
        json.dump(dict(jieba_list),f,ensure_ascii=False)


if __name__ == "__main__":
    main()
