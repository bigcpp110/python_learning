from multiprocessing import Process
import random
import time

"""
函数式多进程
"""

# def hobby_motion(name)->None:
#     print('%s喜欢运动'% name)
#     time.sleep(random.randint(1,3))
#
# def hobby_game(name)->None:
#     print('%s喜欢游戏'% name)
#     time.sleep(random.randint(1,3))
#
# def func(name)->None:
# 	print("%s曾经是好人"%name)
#
# if __name__=="__main__":
# 	# p=Process(target=func,args=("kebi",))
# 	# p.start()
# 	p1 = Process(target=hobby_motion, args=('付婷婷',))
# 	p2 = Process(target=hobby_game, args=('科比',))
# 	p1.start()
# 	p2.start()


"""
类多进程
"""
# class MyProcess(Process):
#     def __init__(self,name:str,age:int):
#         super().__init__()
#         self.name = name
#
#     #重写run方法
#     def run(self)->None:  #start()时，run自动调用，而且此处只能定义为run。
#         print("%s曾经是好人"%self.name)
#
# if __name__ == "__main__":
#     p = MyProcess('kebi',10)
#     p.start()  #将Process当作父类，并且自定义一个函数。


"""
守护进程
p.daemon = True 
"""

# def func(name:str)->None:
#     print("work start:%s"% time.ctime())
#     time.sleep(2)
#     print("work end:%s"% time.ctime())
#
# if __name__ == "__main__":
#     p = Process(target=func,args=('kebi',))
#     p.daemon = True   #父进程终止后自动终止，不能产生新进程，必须在start()之前设置
#     p.start()
#     p.join() # 在进程中可以阻塞主进程的执行, 直到等待子线程全部完成之后, 才继续运行主线程后面的代码
#     print("this is over")

"""
join:p.join()
"""
# import os
# def func(name,hour):
#     print("A lifelong friend:%s,%s"% (name,os.getpid()))
#     time.sleep(hour)
#     print("Good bother:%s"%name)

# if __name__ == "__main__":
# p = Process(target=func,args=('kebi',2))
# p1 = Process(target=func,args=('maoxian',1))
# p2 = Process(target=func,args=('xiaoniao',3))
# p.start()
# p1.start()
# p2.start()
# print("*"*200)
# '''顺序执行'''
# p = Process(target=func,args=('kebi',2))
# p1 = Process(target=func,args=('maoxian',1))
# p2 = Process(target=func,args=('xiaoniao',3))
# p.start()
# p.join()
# p1.start()
# p1.join()
# p2.start()
# p2.join()
# print("this is over")
# print("*"*200)
# """"并行"""
# p = Process(target=func,args=('kebi',2))
# p1 = Process(target=func,args=('maoxian',1))
# p2 = Process(target=func,args=('xiaoniao',3))
# p.start()
# p1.start()
# p2.start()
# p.join()
# p1.join()
# p2.join()
# print("this is over")

"""
terminate:p.terminate()
"""
# def func(name):
#     print("work start:%s"% time.ctime())
#     time.sleep(2)
#     print("work end:%s"% time.ctime())
#
# if __name__ == "__main__":
#     p = Process(target=func,args=('kebi',))
#     p.start()
#     p.terminate()  #将进程杀死，而且必须放在start()后面，与daemon的功能类似


""""
multiprocess.process
参数介绍：

        1. group参数未使用，值始终为None

        2. target表示调用对象，即子进程要执行的任务

        3. args表示调用对象的位置参数元组，args=(1,2,'egon',)

        4. kwargs表示调用对象的字典,kwargs={'name':'egon','age':18}

        5. name为子进程的名称

方法介绍：

       1. p.start()：启动进程，并调用该子进程中的p.run()

        2. p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法

        3. p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁

        4. p.is_alive():如果p仍然运行，返回True 5 p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程

属性介绍：

        1. p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置

        2. p.name:进程的名称

        3. p.pid：进程的pid

        4. p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)

        5. p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）

在Windows操作系统中由于没有fork(linux操作系统中创建进程的机制)，在创建子进程的时候会自动 import 启动它的这个文件，而在 import 的时候又执行了整个文件。因此如果将process()直接写在文件中就会无限递归创建子进程报错。所以必须把创建子进程的部分使用if __name__ ==‘__main__’ 判断保护起来，import 的时候  ，就不会递归运行了。
"""
"""
进程间数据隔离
"""
# from multiprocessing import Process
# import os
# def func():
#     global n        #设置全局环境变量
#     n = 0
#     print('pid : %s' %os.getpid(),n)     #打印这里的pid与n的值
#
# if __name__ == "__main__":
#     n = 100
#     p = Process(target=func)           #注册子进程
#     p.start()       #启动子进程
#     p.join()       #感知子进程的结束
#     print(os.getpid(),n)        #打印父进程的n的值

"""
pid.is_alive
"""
# from multiprocessing import Process
# import time
# def func():
#     while 1:
#         time.sleep(0.5)
#         print('我还活着')
# def func2():
#     print('in func2 start')
#     time.sleep(8)
#     print('in func2 finished')
#
# if __name__ == "__main__":
#     p = Process(target=func)        #func函数注册子进程
#     p.daemon = True      #设置为守护进程，必须在启动子进程之前设置守护进程（守护进程随着主进程的代码执行完成并结束而结束）
#     p.start()     #启动守护进程
#     p2 = Process(target=func2)       #func2函数注册子进程
#     p2.start()       #启动子进程
#     p2.terminate()        #结束一个子进程（系统回收这个进程需要一定得时间）
#     print(p2.is_alive())     #检验一个进程是否活着，True为活着，False为死了，结果为True，表示p2子进程还活着
#     time.sleep(2)
#     print(p2.terminate())     #检验一个进程是否活着，True为活着，False为死了，结果为None，表示p2子进程死了
#     print(p2.name)      #获取当前进程得名字，结果为：Process-2
#     print(p2.pid)       #获取p2进程得pid，结果为：15400
"""
from multiprocessing import Process
def func():
    info = input('>:')        #当子进程中有input时会报错，（即子进程中不能有input）
    print(info)
if __name__ == "__main__":
    Process(target=func).start()

说明：注册子进程的函数中不可以有input，否则会报（EOFError: EOF when reading a line）错！！
"""

"""
进程锁
"""

# import os
# import time
# import random
# from multiprocessing import Process
#
# def work(n):
#     print('%s: %s is running' %(n,os.getpid()))
#     time.sleep(random.random())
#     print('%s:%s is done' %(n,os.getpid()))
#
# if __name__ == '__main__':
#     for i in range(3):
#         p=Process(target=work,args=(i,))
#         p.start()
# import os
# import time
# import random
# from multiprocessing import Process,Lock
#
# def work(lock,n):
#     lock.acquire()       #拿钥匙（拿了钥匙后别的进程就不可以启动了）
#     print('%s: %s is running' % (n, os.getpid()))
#     time.sleep(random.random())
#     print('%s: %s is done' % (n, os.getpid()))
#     lock.release()      #归还钥匙，此时彼得进程才可以拿钥匙进行他的操作
# if __name__ == '__main__':
#     lock=Lock()
#     for i in range(3):
#         p=Process(target=work,args=(lock,i))
#         p.start()
#
# from multiprocessing import Process,Lock
# import time,json,random
# def search():
#     dic=json.load(open('db'))
#     print('\033[43m剩余票数%s\033[0m' %dic['count'])
#
# def get():
#     dic=json.load(open('db'))
#     time.sleep(0.1) #模拟读数据的网络延迟
#     if dic['count'] >0:
#         dic['count']-=1
#         time.sleep(0.2) #模拟写数据的网络延迟
#         json.dump(dic,open('db','w'))
#         print('\033[43m购票成功\033[0m')
#
# def task():
#     search()
#     get()
#
# if __name__ == '__main__':
#     for i in range(100): #模拟并发100个客户端抢票
#         p=Process(target=task)
#         p.start()

# from multiprocessing import Process,Lock
# # import time,json,random
# # def search():
# #     dic=json.load(open('db'))
# #     print('\033[43m剩余票数%s\033[0m' %dic['count'])
# #
# # def get():
# #     dic=json.load(open('db'))
# #     time.sleep(random.random()) #模拟读数据的网络延迟
# #     if dic['count'] >0:
# #         dic['count']-=1
# #         time.sleep(random.random()) #模拟写数据的网络延迟
# #         json.dump(dic,open('db','w'))    #将dic的新值写入到db文件
# #         print('\033[32m购票成功\033[0m')
# #     else:
# #         print('\033[31m购票失败\033[0m')
# #
# # def task(lock):
# #     search()
# #     lock.acquire()      #拿钥匙，此时别的进程就那不到钥匙了
# #     get()     #执行购票函数
# #     lock.release()       #购票成功后还钥匙，还完钥匙后其他进程就可以拿钥匙去购票了
# #
# # if __name__ == '__main__':
# #     lock = Lock()       #实例化一个锁对象
# #     for i in range(100): #模拟并发100个客户端抢票
# #         p=Process(target=task,args=(lock,))      #注册子进程，将锁传入子进程
# #         p.start()     #启动子进程

"""
信号量
互斥锁同时只允许一个线程更改数据，
而信号量Semaphore是同时允许一定数量的线程更改数据 。 
假设商场里有4个迷你唱吧，所以同时可以进去4个人，如果来了第五个人就要在外面等待，
等到有人出来才能再进去玩。 实现： 信号量同步基于内部计数器，每调用一次acquire()，
计数器减1；每调用一次release()，计数器加1.当计数器为0时，acquire()调用被阻塞。这是迪科斯彻（Dijkstra）信号量概念P()和V()的Python实现。
信号量同步机制适用于访问像服务器这样的有限资源。 信号量与进程池的概念很像，但是要区分开，信号量涉及到加锁的概念
"""
# from multiprocessing import Process
# from multiprocessing import Semaphore
# import time
# import random
#
#
# def ktv(i, sem):
#     sem.acquire()  # 获取钥匙
#     print('%s走进ktv' % i)
#     time.sleep(random.randint(1, 5))
#     print('%s走出ktv' % i)
#     sem.release()  # 还钥匙
#
#
# if __name__ == "__main__":
#     sem = Semaphore(4)  # 实例化一个sem对象，传参指定钥匙的数量
#     for i in range(10):
#         p = Process(target=ktv, args=(i, sem))
#         p.start()
"""
事件
python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。

事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，
那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。

clear：将“Flag”设置为False set：将“Flag”设置为True
"""

# from multiprocessing import Event
#
# #一个信号可以使所有的进程都进入阻塞状态，也可以控制所有进程接触阻塞
# #一个事件被创建后，默认是阻塞的状态
#
# e = Event()       #创建一个事件
# print(e.is_set())         #查看一个事件的状态，默认被设置成阻塞，值默认为False
# e.set()       #将这个事件的状态改为True（即非阻塞）
# print(e.is_set())     #结果为：True
# e.wait()      #依据e.is_set（）的值来决定是否阻塞的，e.is_set()的值为False则表示阻塞，可以通过e.set()将e.is_set()的值设置为True则表示不阻塞
# print(123456)
# e.clear()          #将这个事件的状态改为False
# print(e.is_set())    #结果为：False
# e.wait()      #阻塞状态
# print('*'*10)
#
# #set 和 clear
#        #分别用来修改一个事件的状态True或者False
# #is_set用来查看一个事件的状态
# #wait 是依据事件的状态来决定自己是否在wait处阻塞
#       #False：阻塞、True：不阻塞


"""
红绿灯
"""

# from multiprocessing import Process, Event
# import time, random
#
# #is_set() 初始值为false
# def car(e, n):
#     while True:
#         if not e.is_set():  # 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
#             print('\033[31m红灯亮\033[0m，car%s等着\n' % n)
#             e.wait()    # 阻塞，等待is_set()的值变成True，模拟信号灯为绿色
#             print('\033[32m车%s 看见绿灯亮了\n\033[0m' % n)
#             time.sleep(random.randint(3, 6))
#             if not e.is_set():   #如果is_set()的值是Flase，也就是红灯，仍然回到while语句开始
#                 continue
#             print('车开远了,car%s\n'% n)
#             break
#
#
# def police_car(e, n):
#     while True:
#         if  not e.is_set():# 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
#             print('\033[31m红灯亮\033[0m，car%s等着' % n)
#             e.wait(0.1) # 阻塞，等待设置等待时间，等待0.1s之后没有等到绿灯就闯红灯走了
#             if not e.is_set():
#                 print('\033[33m红灯,警车先走\033[0m，car %s' % n)
#             else:
#                 print('\033[33;46m绿灯，警车走\033[0m，car %s' % n)
#         break
#
#
#
# def traffic_lights(e, inverval):
#     while True:
#         time.sleep(inverval)
#         if e.is_set():#如果为绿地
#             print('######', e.is_set())# True绿灯
#             e.clear()  # ---->将is_set()的值设置为False
#         else:
#             e.set()    # ---->将is_set()的值设置为True
#             print('***********',e.is_set())
#
#
# if __name__ == '__main__':
#     e = Event()
#     i=0
#     t = Process(target=traffic_lights, args=(e, 5))  # 创建一个进程控制红绿灯
#     t.start()
#     while True:
#         p=Process(target=car,args=(e,i,))  # 创建是个进程控制10辆车
#         p.start()
#         i+=1
#         time.sleep(random.randint(0,5))
#         # for i in range(5):
#         #     #     p = Process(target=police_car, args=(e, i,))  # 创建5个进程控制5辆警车
#         #     #     p.start()

"""
队列
Queue([maxsize]) 
创建共享的进程队列。maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。底层队列使用管道和锁定实现。另外，还需要运行支持线程以便队列中的数据传输到底层管道中。 
Queue的实例q具有以下方法：

q.get( [ block [ ,timeout ] ] ) 
返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。block用于控制阻塞行为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。

q.get_nowait( ) #无堵塞
同q.get(False)方法。

q.put(item [, block [,timeout ] ] ) 
将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。block控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短。超时后将引发Queue.Full异常。

q.qsize() 
返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。


q.empty() 
如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。

q.full() 
如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的（参考q.empty（）方法）。。

q.close() 
关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，但将在此方法完成时马上关闭。如果q被垃圾收集，将自动调用此方法。关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。例如，如果某个使用者正被阻塞在get（）操作上，关闭生产者中的队列不会导致get（）方法返回错误。

q.cancel_join_thread() 
不会再进程退出时自动连接后台线程。这可以防止join_thread()方法阻塞。

q.join_thread() 
连接队列的后台线程。此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为。

"""
# from multiprocessing import Queue
# q = Queue(5)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)       #往队列中写数据
# print(q.full())     #判断队列是否满了，满了则返回True，未满则返回False
# print(q.get())      #获取队列中的数值
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())      #判断队列是否是空的，为空则则返回True，不为空则返回False
# try:
#     q.get_nowait()      #以非阻塞的形式获取队列中的数值，如果队列里没有数值会报错：quque.Empty
# except:
#     print('队列已空')
# #队列的两种阻塞：1、队列有大小{q = Queue(5)}，写满了再往里写就会产生阻塞，直到队列里面的值有人取走之后才可以继续写入
#             #    2、队列里面已经空了，再从队列里面取值会发生阻塞，直到队列中被写入数据，才可以取到值
# for i in range(6):
#     q.put(i)
#
# from multiprocessing import Queue,Process
#
# def produce(q):
#     print("456")
#     q.put('hello')      #往队列中写入hello
#
# def consume(q):
#     print("123")
#     print('in consume:',q.get())       #从队列中获取hello
#
# if __name__ == "__main__":
#     q = Queue()      #实例化队列
#     p = Process(target=produce,args=(q,))      #注册子进程并将队列以参数的形式传入子进程
#     p.start()       #启动子进程
#     print("你好")
#     c = Process(target=consume,args=(q,))      #注册子进程并将队列以参数的形式传入子进程
#     c.start()        #启用子进程

#
# import os
# import time
# import multiprocessing
#
# # 向queue中输入数据的函数
# def inputQ(queue):
#     info = str(os.getpid()) + '(put):' + str(time.asctime())
#     queue.put(info)
#
# # 向queue中输出数据的函数
# def outputQ(queue):
#     info = queue.get()
#     print ('%s%s\033[32m%s\033[0m'%(str(os.getpid()), '(get):',info))
#
# # Main
# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     record1 = []   # store input processes
#     record2 = []   # store output processes
#     queue = multiprocessing.Queue(3)
#
#     # 输入进程
#     for i in range(10):
#         process = multiprocessing.Process(target=inputQ,args=(queue,))
#         process.start()
#         record1.append(process)
#
#     # 输出进程
#     for i in range(10):
#         process = multiprocessing.Process(target=outputQ,args=(queue,))
#         process.start()
#         record2.append(process)
#
#     for p in record1:
#         p.join()
#
#     for p in record2:
#         p.join()


"""
生产者消费者模型
 在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

为什么要使用生产者和消费者模式
    在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

什么是生产者消费者模式
    生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

"""
#基于队列实现生产者消费者模型
#
# from multiprocessing import Process,Queue
# import time,random,os
# def consumer(q):
#     while True:
#         res=q.get()# 阻塞
#         time.sleep(random.randint(1,3))
#         print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))
#
# def producer(q):
#     for i in range(10):
#         time.sleep(random.randint(1,3))
#         res='包子%s' %i
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,))
#
#     #开始
#     p1.start()
#     c1.start()
#     print('主')
#
# 改良版生产者与消费者模型
# from multiprocessing import Process,Queue
# import time,random,os
# def consumer(q):
#     while True:
#         res=q.get()
#         if res is None:break #收到结束信号则结束
#         time.sleep(random.randint(1,3))
#         print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))
#
# def producer(q):
#     for i in range(10):
#         time.sleep(random.randint(1,3))
#         res='包子%s' %i
#         q.put(res)
#         print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
#     q.put(None) #发送结束信号
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,))
#
#     #开始
#     p1.start()
#     c1.start()
#     print('主')
#主进程在生产者生产完毕后发送结束信号None

#多个消费者的例子：有几个消费者就需要发送几次结束信号
from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        if res is None:break #收到结束信号则结束
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(name,q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        res='%s%s' %(name,i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=('包子',q))
    p2=Process(target=producer,args=('骨头',q))
    p3=Process(target=producer,args=('泔水',q))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))
    c2=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()

    p1.join() #必须保证生产者全部生产完毕,才应该发送结束信号
    p2.join()
    p3.join()
    q.put(None) #有几个消费者就应该发送几次结束信号None
    q.put(None) #发送结束信号
    print('主')
