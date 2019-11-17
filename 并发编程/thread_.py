# import time
# import random
# from threading import Thread
#
# def piao(name):
#     print("%s is running " % name)
#     time.sleep(random.randrange(1,3))
#     print("%s run end" % name)
#
# if __name__=="__main__":
#     t1=Thread(target=piao,args=("qiuma",))
#     t1.start()
#     print("main process end")


import time
import random
from threading import Thread


class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("%s run end" % self.name)
        time.sleep(random.randrange(1,3))
        print("%s run end" % self.name)


if __name__=="__main__":
    t1=MyThread("quima")
    t1.start()
    print("main process end")