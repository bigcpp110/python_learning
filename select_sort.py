import random

def select_sort(li):
    temp=0
    n=len(li)
    for i in range(n):
        for j in range(i,n):
            if li[j]>li[temp]:
                li[i],li[j]=li[j],li[i]
        temp+=1
    return li

li=list(range(10))
random.shuffle(li)
print(select_sort(li))
