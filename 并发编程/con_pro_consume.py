import threading
import time

con=threading.Condition()

num=0


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global num
        con.acquire()
        while True:
            print("开始添加")
            num+=1
            print("火锅里面鱼丸个数: %s"%num)
            time.sleep(1)
            if num>=5:
                print("鱼丸数量已经达到5个，已经无法添加了")
                con.notify()
                con.wait()
        con.release()


class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while True:
            print("开始吃啦")
            num-=1
            print("鱼丸剩余数量:%s" % num)
            time.sleep(2)
            if num<0:
                print("锅底没货啦，赶紧加鱼丸吧")
                con.notify()
                con.wait()
        con.release()


if __name__=="__main__":
    p=Producer()
    c=Consumers()
    p.start()
    c.start()