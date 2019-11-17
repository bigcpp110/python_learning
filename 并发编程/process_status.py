from multiprocessing import Process
import os,time



def task():
    print("%s is running,parent id is %s"%(os.getpid(),os.getppid()))
    time.sleep(3)
    print("%s is done,parent id is %s" % (os.getpid(), os.getppid()))



if __name__=="__main__":
    p=Process(target=task)
    p.start()
    p.join()
    print('主', os.getpid(), os.getppid())
    print(p.pid)


    p=Process(target=task,name="sub_process")
    p.start()
    p.terminate()
    time.sleep(3)
    print(p.is_alive())
    print(p.name)