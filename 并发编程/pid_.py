# import os
#
#
# print(os.cpu_count())


from multiprocessing import Process
import time
import random
import os


def task(name):
    print("%s is running" % name)
    time.sleep(1)
    print("%s is done" % name)


def write(name):
    print("%s is writing" % name)
    time.sleep(random.randint(1,5))
    print("%s end write" % name)



if __name__=="__main__":
    p=Process(target=task,args=("subprocess_1",))
    p.start()
    print("%s %s" % (os.getpid(),os.getppid()))

