from cal_time import cal_time
import random

@cal_time
def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)


def qsort(ary, start, end):
    if start < end:
        left = start
        right = end
        key = ary[start]
    else:
        return ary
    while left < right:
        while left < right and ary[right] >= key:
            right -= 1
        if left < right:  # 说明打破while循环的原因是ary[right] <= key
            ary[left] = ary[right]
            left += 1
        while left < right and ary[left] < key:
            left += 1
        if left < right:  # 说明打破while循环的原因是ary[left] >= key
            ary[right] = ary[left]
            right -= 1
    ary[left] = key  # 此时，left=right，用key来填坑

    qsort(ary, start, left - 1)
    qsort(ary, left + 1, end)
    return ary

li=list(range(0,10000))
random.shuffle(li)
quick_sort(li)
print(li)