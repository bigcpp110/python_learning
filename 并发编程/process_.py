# import os
#
#
# print(os.cpu_count())


from multiprocessing import Process
import time
import random


def task(name):
    print("%s is running" % name)
    time.sleep(1)
    print("%s is done" % name)


def write(name):
    print("%s is writing" % name)
    time.sleep(random.randint(1,5))
    print("%s end write" % name)



if __name__=="__main__":
    # p=Process(target=task,args=("subprocess_1",))
    # p.start()
    # print("main process end")
    p1=Process(target=write,args=("egon",))
    p2 = Process(target=write, args=("alex",))
    p3 = Process(target=write, args=("wupeqi",))
    p4 = Process(target=write, args=("yuanhao",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print("main process end")
