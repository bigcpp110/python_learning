from cal_time import cal_time
import random

@cal_time
def insert_sort(li):
    n=len(li)
    for i in range(1,n):
        p=i-1
        tmp=li[i]
        while p>=0 and li[p]>tmp:
            li[p+1]=li[p]
            p-=1
        li[p+1]=tmp
    return li



li=list(range(0,10000))
random.shuffle(li)
insert_sort(li)
print(li)