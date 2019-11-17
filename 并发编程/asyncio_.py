import asyncio
import time


async def get_html(url):
    print("start get url:%s" % url)
    await asyncio.sleep(2)
    print("end get url:%s" %url )

if __name__=="__main__":
    start_time=time.time()
    loop=asyncio.get_event_loop()
    tasks=[get_html("http://www.imooc.com") for _ in range(10) ]
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:%s"%(time.time()-start_time))