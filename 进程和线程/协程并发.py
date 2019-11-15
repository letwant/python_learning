import asyncio

import time

now = lambda: time.time()


async def do_some_work(x):
    print('Waiting: ', x)

    time.sleep(x)
    print(x)
    return 'Done after {}s'.format(x)


start = now()

# async def foo1():
#     print(111)
#     await asyncio.sleep(2)
#     print(444)
#
# async def foo2():
#     print(222)
#     await asyncio.sleep(2)
#     print(555)
#
# async def foo3():
#     print(333)
#     await asyncio.sleep(2)
#     print(666)


def foo():
    tasks = [asyncio.ensure_future(do_some_work(2))] * 3
    # tasks = list(map(asyncio.ensure_future, [foo1(), foo2(), foo3()]))


    # coroutine1 = do_some_work(1)
    # coroutine2 = do_some_work(2)
    # coroutine3 = do_some_work(4)
    #
    # tasks = [
    #     asyncio.ensure_future(coroutine1),
    #     asyncio.ensure_future(coroutine2),
    #     asyncio.ensure_future(coroutine3)
    # ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print('Task ret: ', task.result())

    print('TIME: ', now() - start)


foo()