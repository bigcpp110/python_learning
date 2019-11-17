from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print("%s say hello" % name)


def foo():
    print(123)
    time.sleep(0.5)
    print("end 123")

def bar():
    print(456)
    time.sleep(1)
    print("end 456")

if __name__=="__main__":
    # t=Thread(target=sayhi,args=("qiuma",))
    # t.daemon=True
    # t.start()
    # print("main process is done")
    # print(t.is_alive())
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main process end")