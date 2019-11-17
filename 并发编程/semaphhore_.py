from threading import Thread,Semaphore,current_thread
import random,time

sm=Semaphore(3)


def task():
    with sm:
        print("%s in "% current_thread().getName())
        time.sleep(random.randint(1,2))



if __name__=="__main__":
    for i in range(10):
        t=Thread(target=task)
        t.start()

