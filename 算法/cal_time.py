import time

def cal_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(end_time-start_time)
    return wrapper