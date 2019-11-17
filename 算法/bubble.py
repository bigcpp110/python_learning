from cal_time import cal_time
import random


@cal_time
def bubble(li):
    ln=len(li)
    for i in range(0,ln-1):
        flag=True
        for j in \
                range(ln-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                flag=False
        if flag:
            return





li=list(range(0,10000))
random.shuffle(li)
bubble(li)
print(li)