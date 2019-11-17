"""
yield 版
"""
# #字符串
# astr="ABC"
# #列表
# alist=[1,2,3]
# #字典
# adict={"name":"wangbm","age":18}
# #生成器
# agen=(i for i in range(4,8))
# def gen(*args,**kwargs):
#     for item in args:
#         for i in item:
#             yield i
#
#
# new_list=gen(astr,alist,adict,agen)
# print(list(gen(new_list)))

"""
yield from
"""
# #字符串
# astr="ABC"
# #列表
# alist=[1,2,3]
# #字典
# adict={"name":"wangbm","age":18}
# #生成器
# agen=(i for i in range(4,8))
#
# def gen(*args,**kwargs):
#     for item in args:
#         yield from item
#
# new_list=gen(astr, alist, adict, agen)
# print(list(new_list))

def average_gen():
    total=0
    count=0
    average=0
    while True:
        new_num=yield average
        count+=1
        total+=new_num
        average=total/count

def proxy_gen():
    while True:
        yield from average_gen()

def main():
    calc_average=proxy_gen()
    next(calc_average)
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))

if __name__=="__main__":
    main()
