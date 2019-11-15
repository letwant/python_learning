import asyncio
import time

async def foo():
    print('wwwwwwwww')
    await sleep()
    print('11111111')
    return 222


async def sleep():

    return time.sleep(3)


async def foo1():
    print(333333333)
    await sleep()
    print('5555555555555')
    return 1


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(foo()), asyncio.ensure_future(foo1())]
    data, pending = loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(222222222222)