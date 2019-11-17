from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("%s is running" % self.name)
        time.sleep(1)
        print("%s is done" % self.name)


if __name__=="__main__":
    p=MyProcess("subprocess_1")
    p.start()
    print("main process end")