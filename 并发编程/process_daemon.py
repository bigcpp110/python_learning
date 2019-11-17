from multiprocessing import Process
import time


def task(name):
    print("%s is running" % name)
    time.sleep(2)
    print("%s is done" % name)


if __name__=="__main__":
    p=Process(target=task,args=("subprocess_1",))
    p2 = Process(target=task, args=("subprocess_2",))
    p.daemon=True
    p.start()
    p2.start()
    # p.join()
    print("main process end")