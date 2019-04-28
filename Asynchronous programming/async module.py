# @Time    : 2019/4/28 14:48
# @Author  : Noah
# @File    : async module.py
# @Software: PyCharm
# @description: async和await是针对协程coroutine的新语法
import asyncio


async def hello():
    print("Hello world!")
    await asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
