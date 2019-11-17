from threading import Thread,Lock
import time


lock_a=Lock()
lock_b=Lock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        lock_a.acquire()
        print("%s 拿到了A锁" % self.name)
        lock_b.acquire()
        print("%s 拿到了B锁"%self.name)
        lock_a.release()
        lock_b.release()

    def f2(self):
        lock_b.acquire()
        time.sleep(0.1)
        lock_a.acquire()
        print('%s 拿到了A锁' % self.name)
        lock_a.release()

        lock_b.release()



if __name__=="__main__":
    for _ in range(10):
        t=MyThread()
        t.start()