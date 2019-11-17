import asyncio
import time



async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.gather(*tasks))
    # group1=[get_html("http://www.imooc.com") for i in range(5)]
    # group2=[get_html("http://www.imooc.com") for i in range(5)]
    #
    # group1=asyncio.gather(*group1)
    # group2=asyncio.gather(*group2)
    # group2.cancel()
    # loop.run_until_complete(asyncio.gather(group1,group2))
    print("last time:%s"%(time.time()-start_time))


