from threading import Thread,Event
import time


event=Event()

def student(name):
    print("学生%s正在听课" % name)
    event.wait(2) #阻塞
    print("学生%s课间活动" % name)


def teacher(name):
    print("老师%s正在授课"%name)
    time.sleep(7)
    event.set() #释放锁

if __name__ == '__main__':
    stu1 = Thread(target=student,args=('alex',))
    stu2 = Thread(target=student,args=('wxx',))
    stu3 = Thread(target=student,args=('yxx',))
    t1 = Thread(target=teacher,args=('egon',))

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()