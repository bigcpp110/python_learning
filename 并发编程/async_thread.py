import asyncio
from concurrent.futures import ThreadPoolExecutor



def get_url(url):
    print("start crawl %s" % url)
    time.sleep(2)

if __name__=="__main__":
    import time
    start=time.time()
    loop=asyncio.get_event_loop()
    executor=ThreadPoolExecutor()
    tasks=[]
    for url in range(20):
        url="https://www.baidu.com/{}".format(url)
        task=loop.run_in_executor(executor,get_url,url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:%s" % (time.time()-start))