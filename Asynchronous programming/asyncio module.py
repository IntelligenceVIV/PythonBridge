# @Time    : 2019/4/22 0:56
# @Author  : Noah
# @File    :
# @Software: PyCharm
# @description: 是一个使用async / await语法编写并发代码的库

# 内置对异步IO的支持
import asyncio
import datetime
import time

from asyncio import CancelledError


###########################################################################
async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


asyncio.run(main())

###########################################################################
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello')
    )
    task2 = asyncio.create_task(
        say_after(2, 'world')
    )
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


###########################################################################
async def nested():
    return 42


async def main():
    task = asyncio.create_task(nested())
    await task


asyncio.run(main())


###########################################################################
async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0

    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


asyncio.run(display_date())


###########################################################################
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


asyncio.run(main())


###########################################################################
async def something():
    pass


async def main():
    try:
        res = await asyncio.shield(something())
    except CancelledError:
        res = None

    try:
        await asyncio.wait_for(something(), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")


asyncio.run(main())

###########################################################################

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

###########################################################################
