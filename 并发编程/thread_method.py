from threading import Thread,current_thread,active_count,enumerate
import time



def task():
    print("%s is running"%current_thread().getName())
    time.sleep(2)
    print("%s is done" % current_thread().getName())


if __name__=="__main__":
    t=Thread(target=task,name="subprocess_1")
    t.start()
    t.setName(("subprocess_2"))
    t.join()
    print(enumerate())
    print(t.getName())
    current_thread().setName("main process")
    print(t.is_alive())

    print("main process: %s"%current_thread().getName())
    t.join()
    print(enumerate())
    print(active_count())
    print(enumerate())
