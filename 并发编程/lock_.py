from multiprocessing import Process,Lock
import time

def task(name,lock):
    lock.acquire()
    print("%s 1" % name)
    time.sleep(1)
    print("%s 2" % name)
    time.sleep(1)
    print("%s 3" % name)
    lock.release()



if __name__=="__main__":
    lock=Lock()
    for i in range(3):
        p=Process(target=task,args=("subprocess%s"%i,lock))
        p.start()

