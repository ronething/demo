# -*- coding:utf-8 _*-  
""" 
@author: ashing 
@time: 2020-02-01 16:11
@mail: axingfly@gmail.com

Less is more.
"""

import asyncio


# 加上 async 协程对象 不是函数
async def print_hello():
    while True:
        print("hello world")
        await asyncio.sleep(1)


async def print_goodbye():
    while True:
        print("hello goodbye")
        await asyncio.sleep(2)


if __name__ == '__main__':
    co1 = print_hello()
    co2 = print_goodbye()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(co1, co2))
