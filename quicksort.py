import random
import sys

# sys.setrecursionlimit(30000000) # 设置最大递归深度为3000


def quick_sort(li):
    if len(li)<2:
        return li
    mid=li[len(li)//2]
    left =[]
    right=[]
    li.remove(mid)
    for v in li:
        if v >mid:
            right.append(v)
        else:
            left.append(v)
    return quick_sort(left)+[mid]+quick_sort(right)


li=list(range(15))
random.shuffle(li)
print(quick_sort(li))