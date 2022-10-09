# -*- coding:utf-8 _*-  
""" 
@author: ashing 
@time: 2020-02-01 16:17
@mail: axingfly@gmail.com

Less is more.
"""

# crontab 调度器 每秒拉起一个 job，job 会并发爬取网页

import asyncio
import random
import functools
from asyncio import Task


def print_res(res: Task):
    if not res.exception():
        print(res.result())
    else:
        # 发生异常
        print(res)
    # print(res._result)


async def cron_scheduler():
    page = 1
    while True:
        # await asyncio.sleep(0.2)
        job = cron_job(F"https://baidu.com/{page}")
        # await job # 在当前协程中等待其他协程完成 会阻塞
        # 正确做法 create_task 将 job 分离出去 由 loop 调度
        a = asyncio.create_task(job)  # 注册到时间循环
        # a = asyncio.ensure_future(job) # 跟 task 的作用类似 比 task api 级别底层
        a.add_done_callback(functools.partial(print_res))
        await asyncio.sleep(0)  # 主动让出资源调度
        page = page + 1


async def cron_job(i: str):
    while True:
        await asyncio.sleep(random.randint(1, 3))  # 网络延迟
        # print("爬取网页中", i)
        return i


if __name__ == '__main__':
    c1 = cron_scheduler()

    loop = asyncio.get_event_loop()  # epoll
    loop.run_until_complete(c1)
