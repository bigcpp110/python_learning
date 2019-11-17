from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random


def task(name):
    print("name:%s pid:%s run " % (name,os.getpid()))
    time.sleep(random.randint(1,3))


if __name__=="__main__":
    excutor=ProcessPoolExecutor(4) #最大同时运行的进程数
    excutor=ThreadPoolExecutor(5)

    for i in range(10):
        excutor.submit(task,"qiuma %s" % i)

    excutor.shutdown(wait=True)
    print("main process end")