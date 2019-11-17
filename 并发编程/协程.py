import time
import asyncio

now=lambda :time.time()

async  def do_some_work(x):
    print("waiting: %s" % x)


start=now()

coroutine=do_some_work(2)
print(coroutine)
loop=asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("lasttime: %s" % (now()-start))

