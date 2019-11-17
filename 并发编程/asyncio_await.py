import asyncio
import time

now=lambda:time.time()

async def do_some_work(x):
    print("waiting:%s" % x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start=now()
coroutine=do_some_work(2)
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task ret:%s"%task.result())
print("last time:%s"%(now()-start))

