from cal_time import cal_time
import random

@cal_time
def select_sort(li):
    n=len(li)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if li[j]<li[min]:
                min=j
        li[min],li[i]=li[i],li[min]

    return li

li=list(range(0,10000))
random.shuffle(li)
select_sort(li)
print(li)