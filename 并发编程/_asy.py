# import asyncio
# import time
#
#
# async def main():
#     print('Hello ...')
#     time.sleep(1)
#     await asyncio.sleep(1)
#     print('... World!')


# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# # async def main():
# #     print(f"started at {time.strftime('%X')}")
# #     await say_after(1, 'hello')
# #     await say_after(2, 'world')
# #     print(f"finished at {time.strftime('%X')}")
#
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())

#
# import asyncio
#
# async def nested():
#     return 42
#
# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     await task
# asyncio.run(main())
#
# import selectors
# import socket
#
# sel = selectors.DefaultSelector()
#
# def accept(sock, mask):
#     conn, addr = sock.accept()  # Should be ready
#     print('accepted', conn, 'from', addr)
#     conn.setblocking(False)
#     sel.register(conn, selectors.EVENT_READ, read)
#
# def read(conn, mask):
#     data = conn.recv(1000)  # Should be ready
#     if data:
#         print('echoing', repr(data), 'to', conn)
#         conn.send(data)  # Hope it won't block
#     else:
#         print('closing', conn)
#         sel.unregister(conn)
#         conn.close()
#
# sock = socket.socket()
# sock.bind(('localhost', 1234))
# sock.listen(100)
# sock.setblocking(False)
# sel.register(sock, selectors.EVENT_READ, accept)
#
# while True:
#     events = sel.select()
#     for key, mask in events:
#         callback = key.data
#         callback(key.fileobj, mask)


# import time
# import asyncio
#
# # 定义异步函数
# async def hello():
#     await asyncio.sleep(1)
#     print('Hello World:%s' % time.time())
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
# loop = asyncio.get_event_loop()
# if __name__ =='__main__':
#     run()


# import asyncio
# from aiohttp import ClientSession
#
#
# tasks = []
# url = "https://www.baidu.com/{}"
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#             print(response)
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(hello(url))


# import time
# import asyncio
#
#
# now = lambda : time.time()
#
#
# async def do_some_work(x):
#     print("waiting:",x)
#     return "Done after {}s".format(x)
#
#
# def callback(future):
#     print("callback:",future.result())
#
#
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# print(task)
# task.add_done_callback(callback)
# print(task)
# loop.run_until_complete(task)
#
# print("Time:", now()-start)


import asyncio
import time



now = lambda :time.time()
@asyncio.coroutine
def do_some_work(x):
    print("waiting:",x)
    # await 后面就是调用耗时的操作
    yield from asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task ret:", task.result())
print("Time:", now() - start)