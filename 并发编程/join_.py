import time,os
from multiprocessing import Process


def task():
    print("%s is running,parent id is <%s>" % (os.getpid(),os.getppid()))
    time.sleep(1)
    print("%s is done,parent id is <%s>" % (os.getpid(),os.getppid()))

def task2(name,n):
    print("%s is running" % name)
    time.sleep(n)


if __name__=="__main__":
    # p=Process(target=task)
    # p.start()
    #
    # p.join()
    #
    # print("sub process is %s ,mai process is %s" % (os.getpid(),os.getppid()))
    #
    # print(p.pid)

    # """
    # 并发版
    # """
    # start=time.time()
    # p1=Process(target=task2,args=("subprocess_1",3))
    # p2 = Process(target=task2, args=("subprocess_2", 1))
    # p3 = Process(target=task2, args=("subprocess_3", 2))
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    #
    # print("last time %s" %(time.time()-start))


    """
    并行版
    """
    start=time.time()
    p1=Process(target=task2,args=("subprocess_1",3))
    p2 = Process(target=task2, args=("subprocess_2", 1))
    p3 = Process(target=task2, args=("subprocess_3", 2))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()

    print("last time %s" %(time.time()-start))

