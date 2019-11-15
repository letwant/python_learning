import asyncio
import time


now = lambda :time.time()


async def foo(x):
    return await do_some_work(x)

async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

start = now()



data = []
for i in range(1, 4):
    dd = foo(i)
    data.append(dd)



tasks = [asyncio.ensure_future(coroutine) for coroutine in data]
print(tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:",task.result())

print("Time:",now()-start)