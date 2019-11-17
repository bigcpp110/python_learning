import time
import asyncio

now=lambda :time.time()

async def do_some_work(x):
    print("waiting: %s" % x)
    return "Done after {}s".format(x)


def callback(future):
    print("callback: %s" %future.result())


start=now()
coroutine=do_some_work(2)
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(coroutine)
print(task)
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)
print("last time:%s" % (now()-start))