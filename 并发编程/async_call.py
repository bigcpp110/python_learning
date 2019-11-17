import asyncio

def callback(sleep_times,loop):
    print("success time {}".format(loop.time()))

def stoploop(loop):
    print("loop 结束")
    loop.stop()


if __name__=="__main__":
    import time
    start=time.time()
    loop=asyncio.get_event_loop()
    now=loop.time()
    loop.call_at(now+2,callback,2,loop)
    loop.call_at(now+3,stoploop,loop)
    loop.run_forever()
    print("last time: %s" % (time.time()-start))