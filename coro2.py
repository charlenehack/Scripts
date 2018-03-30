#!/usr/bin/env python3
# coding:utf8

import asyncio

import requests


async def coro2(num):
    # await asyncio.sleep(5)
    return 2

async def coro1(num):
    print('coro %s is runing' % num)
    # X是协程coro2的返回值。这里是2
    x = await coro2(num)
    print('coro %s runing again' % num)
    return 2


async def get_page(url):
    return requests.get(url).tet

#注意，这里是普通函数.回调函数的最后一个参数是futu
# futu就是协程对象本身，result就是协程运行完的结果
def parse_page(futu):
    print(futu.result())


# 要让协程运行的方式，一是在另一个协程中用await等待它。
# 通过asynio.ensure_future或者loop.create包装成task对象给run_until_complete运行
#
# task对象是Future类的子类,保存了协程运行后的状态，用于未来获取协程的结果

# tasks = [ asyncio.ensure_future(coro1(i)) for i in range(5,10) ]
# loop = asyncio.get_event_loop()
# 如果要运行多个协程，就需要用asyncio.gather.
# loop.run_until_complete(asyncio.gather(*tasks))

# 回调
loop = asyncio.get_event_loop()
futu = asyncio.ensure_future(get_page('http://www.baidu.com/'))
futu.add_done_callback(parse_page)
loop.run_until_complete(futu)
loop.close()

#　如果回调函数需要传入多个参数。通过偏函数
def callback(t, futu):
    print('callback', t, futu.result())

task.add_done_callback(functools.partial(callback, 2))
