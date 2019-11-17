from threading import Thread,Event,current_thread
import time

event=Event()

def conn():
    n=0
    while not event.is_set():
        if n==3:
            print("%s try too many times" % current_thread().getName())
            return
        print("%s try %s" % (current_thread().getName(),n))
        event.wait(0.5)
        n+=1

    print("%s is connected" % current_thread().getName())


def check():
    print("%s is checking" % current_thread().getName())
    time.sleep(2)
    event.set()



if __name__=="__main__":
    for i in range(3):
        t=Thread(target=conn)
        t.start()
    t=Thread(target=check)
    t.start()
