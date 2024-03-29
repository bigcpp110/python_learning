# import asyncio
# from threading import Thread
# import time
#
#
#
# now=lambda :time.time()
#
# def start_loop(loop):
#     asyncio.set_event_loop(loop)
#     loop.run_forever()
#
# def more_work(x):
#     print("more work {}".format(x))
#     time.sleep(x)
#     print("Finished more work {}".format(x))
#
# start=now()
# new_loop=asyncio.new_event_loop()
# t=Thread(target=start_loop,args=(new_loop,))
# t.start()
# print('TIME: {}'.format(time.time() - start))
# new_loop.call_soon_threadsafe(more_work,6)
# new_loop.call_soon_threadsafe(more_work,3)



import asyncio
from threading import Thread
import time



now=lambda :time.time()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))

def more_work(x):
    print("more work {}".format(x))
    time.sleep(x)
    print("Finished more work {}".format(x))

start=now()
new_loop=asyncio.new_event_loop()
t=Thread(target=start_loop,args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))
new_loop.call_soon_threadsafe(more_work,6)
new_loop.call_soon_threadsafe(more_work,3)
print("main process end")
