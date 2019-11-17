def gen():
    v=1
    while True:
        yield v
        v+=1


# g=gen()
# print(next(g))
# print(next(g))
# print(g.__next__())
# print(g.throw(Exception, "Method throw called!"))



# def gen():
#     v=1
#     while True:
#         try:
#             yield v
#         except:
#             v+=1
#
#
# # g=gen()
# # # print(next(g))
# # # print(next(g))
# # # print(g.__next__())
# # # print(g.throw(Exception, "Method throw called!"))
#
#
# def gen():
#     n = 0
#     while True:
#         try:
#             yield n
#             n += 1
#         except ZeroDivisionError:
#             print('捕获到了 ZeroDivisionError')
#             print('此时的 n 为：%s' % n)
#
# g = gen()
# ret = next(g)
# print('第一次 yield 的返回值：%s' % ret)
# """
# 第一次 yield 的返回值：0
# """
#
# print()
# ret = g.throw(ZeroDivisionError)
# print('第二次 yield 的返回值：%s' % ret) # 在生成器暂停的地方抛出类型为 type 的异常，并返回下一个 yield 的返回值
# """
# 捕获到了 ZeroDivisionError
# 此时的 n 为：0
# 第二次 yield 的返回值：0
# """
#
# print()
# ret = next(g)
# print('第三次 yield 的返回值：%s' % ret)
# """
# 第三次 yield 的返回值：1
# """
#
#
#
# import sys
#
# def gen():
#     n = 0
#     while True:
#         yield n
#         n += 1
#
# g = gen()
# ret1 = next(g)
# print('第一次 yield 的返回值：%s' % ret1)
# """
# 第一次 yield 的返回值：0
# """
#
# print()
# try:
#     ret2 = g.throw(ZeroDivisionError)  # ret2 并没有收到任何值
# except ZeroDivisionError:
#     print('调用方捕获到 ZeroDivisionError 异常')
#     print(sys.exc_info())
# """
# 调用方捕获到 ZeroDivisionError 异常
# (<class 'ZeroDivisionError'>, ZeroDivisionError(), <traceback object at 0x0000028E8AA10148>)
# """
#
# print()
# # 因为赋值没有发生就抛出了异常，所以变量 ret2 还不存在
# try:
#     print("ret2: %s" % ret2)
# except NameError:
#     print('捕获到了 NameError')
#     print(sys.exc_info())
# """
# 捕获到了 NameError
# (<class 'NameError'>, NameError("name 'ret2' is not defined"), <traceback object at 0x000001C624DB0248>)
# """
#
# print()
# print('尝试再次从生成器中获取值')
# print(next(g))
# """
# 尝试再次从生成器中获取值
# Traceback (most recent call last):
#   File "test.py", line 41, in <module>
#     print(next(g))
# StopIteration
# """


print("---------第三种情况-----------------")

"""
第三种情况
"""
import sys

def gen():
    try:
        # 注意是在当前暂停的 yield 处抛出异常
        # 所以要在这里捕获
        yield 1
    except Exception as e:
        print('在生成器内部捕获了异常')
        print(e.args)
        print('处理完毕，假装什么也没发生')
        print()

    yield 2

g = gen()
print(next(g))
"""
1
"""

print()
g.throw(TypeError, '类型错误哟~')
"""
在生成器内部捕获了异常
('类型错误哟~',)
处理完毕，假装什么也没发生

Traceback (most recent call last):
  File "test.py", line 23, in <module>
    g.throw(TypeError, '类型错误哟~')
StopIteration
"""

