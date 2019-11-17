import time
from threading import Thread
from multiprocessing import Process


def run(name):
    print("%s running "% name)
    time.sleep(2)
    print("%s run end" % name)

if __name__=="__main__":
    # t1=Thread(target=run,args=("qiuma",))
    # t1.start()
    # print("main process end")

    p1 = Process(target=run, args=("qiuma",))
    p1.start()
    print("main process end")

