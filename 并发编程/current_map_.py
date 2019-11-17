from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import os,time,random

def task(n):
    print("%s is running" % os.getpid())
    time.sleep(random.randint(1,3))
    return n**2


if __name__=="__main__":
    executor=ThreadPoolExecutor(max_workers=3)
    f=executor.map(task,range(1,12))
    print(f.result())