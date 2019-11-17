# from threading import Thread
# import os
#
#
# def task():
#     print("sub_process:%s"%(os.getpid()))
#
#
#
# if __name__=="__main__":
#     t1=Thread(target=task)
#     t2=Thread(target=task)
#     t1.start()
#     t2.start()
#     print("main process: %s"%os.getpid())


from threading import Thread


n=100

def task():
    global n
    n=0


if __name__=="__main__":
    t1=Thread(target=task)
    t1.start()
    t1.join()
    print("main process %d" % n)