from threading import Thread,Lock
import time


n=100


def task():
    global n
    lock.acquire()
    temp=n
    time.sleep(0.5)
    n=temp-1
    lock.release()


if __name__=="__main__":
    lock=Lock()
    t_1=[]
    for _ in range(100):
        t=Thread(target=task)
        t_1.append(t)
        t.start()

    for t in t_1:
        t.join()

    print("main process n is : %d" % n)
