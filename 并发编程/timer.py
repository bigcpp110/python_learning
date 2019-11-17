from threading import Timer
import time

def hello():
    print("hello world")


start=time.time()
t=Timer(3,hello)#非阻塞
t.start()
for _ in range(3):
    time.sleep(1)
print(time.time()-start)