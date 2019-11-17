from cal_time import cal_time
import random


def merge_sort(li):
    if len(li)<=1:
        return li
    mid=len(li)//2
    left=merge_sort(li[:mid])
    right=merge_sort(li[mid:])
    return merge(left,right)


def merge(left,right):
    res=[]
    i = j = k = 0
    while (i<len(left) and j < len(right)):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res=res+left[i:]+right[j:]
    return res

li=list(range(0,10000))
random.shuffle(li)
merge_sort(li)
print(li)