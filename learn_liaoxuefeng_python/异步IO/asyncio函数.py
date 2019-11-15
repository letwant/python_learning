import asyncio


# async def hello():
#     print("hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = await asyncio.sleep(1)
#     print("hello again!")
#
# # 获取EventLoop:
# asyncio.run(hello())

# async def main():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#     asyncio.run(main())



import threading

# @asyncio.coroutine
# def hello1():
#     print('Hello World! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello1(), hello1()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

# async def wget(host):
#     print('wget {}...'.format(host))
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('{0} header > {1}'.format(host, line.decode('utf-8')).rstrip())
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com', 'www.baidu.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()