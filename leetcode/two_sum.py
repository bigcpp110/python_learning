

def two_sum(nums,target):
    d=[]
    for num in nums:
        if (target-num) in nums:
            d.append((num,target-num))
    return d

def twoSum(nums,target):
    d={}
    for i,num in enumerate(nums):
        if target-num in d:
            return [d[target-num],i]
        d[num]=i


nums=[11,2,7,15]
target=9
ret=twoSum(nums,target)
print(ret)