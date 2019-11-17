from threading import Thread,RLock
import time


lockA=lockB=RLock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        lockA.acquire()
        print('%s 拿到了A锁' % self.name)

        lockB.acquire()
        print('%s 拿到了B锁' % self.name)
        lockB.release()

        lockA.release()

    def f2(self):
        lockB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(0.1)

        lockA.acquire()
        print('%s 拿到了A锁' % self.name)
        lockA.release()

        lockB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()