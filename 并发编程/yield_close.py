# import re
#
#
# def cortoutine(func):
#     def start(*args,**kwargs):
#         cr=func(*args,**kwargs)
#         next(cr)
#         return cr
#     return start
#
# @cortoutine
# def grep(pattern):
#     pattern=re.compile(pattern)
#     while True:
#         line=(yield )
#         m=pattern.search(line)
#         if m:
#             print(m.string)
#
# g=grep(r"^abc")
# g.send("abcd")
# g.close()
# g.send("1abcd")



"""
第一种情况
"""
# def gen():
#     print('下面 yield 1')
#     yield 1
#     print('下面 yield 2')
#     yield 2
#
# g = gen()
# next(g)
# g.close()
# """
# 下面 yield 1
# """
#
# print()
# next(g)
# """
# Traceback (most recent call last):
#   File "test.py", line 15, in <module>
#     next(g)
# StopIteration
# """
"""
generator.close()
作用：在生成器函数暂停的地方抛出一个 GeneratorExit 异常。
这并不等价于 generator.throw(GeneratorExit)，后面会说原因。
如果生成器抛出 StopIteration 异常（不管是由于正常退出还是因为该生成器已经关闭），或者抛出 GeneratorExit 异常（不捕获该异常即可），close 方法不传递该异常，直接返回到调用方。而生成器抛出的其他异常会传递给调用方。
GeneratorExit 异常的产生意味着生成器对象的生命周期已经结束，因此生成器方法后续语句中不能再有 yield，否则会产生 RuntimeError。（而 throw 方法是期待一个 yield 返回值的，如果没有，则会抛出 StopIteration 异常。）
对于已经正常退出或者因为异常退出的生成器对象，close 方法不会进行任何操作。
"""

"""
第一种情况：不捕获 GeneratorExit 异常，close 方法返回调用方，不传递该异常
"""
def gen():
    print('下面 yield 1')
    yield 1
    print('下面 yield 2')
    yield 2

g = gen()
next(g)
g.close()
"""
下面 yield 1
"""

print()
next(g)
"""
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    next(g)
StopIteration
"""



"""
第二种情况：生成器自然退出抛出 StopIteration 异常，该异常不会传递给调用方，close 方法正常返回。
"""

def gen():
    try:
        yield 1
    except GeneratorExit:
        print('捕获到GeneratorExit')
    print('生成器函数结束了')

g = gen()
print(next(g))
g.close()
"""
1
捕获到GeneratorExit
生成器函数结束了
"""

"""
第三种情况：在 GeneratorExit 抛出后还有 yield 语句，会产生 RuntimeError。另外生成器对象被垃圾回收时，解释器会自动调用该对象的 close 方法（PEP 342），这意味着最好不要在相应的 except 和 finally 中写 yield 语句，否则不知道什么时候就会抛出 RuntimeError 异常
"""
# def gen():
#     try:
#         yield 1
#     except GeneratorExit:
#         print('捕获到 GeneratorExit')
#         print('尝试在 GeneratorExit 产生后 yield 一个值')
#         yield 2
#
#     print('生成器结束')
#
#
# g = gen()
# next(g)
# g.close()
# """
# 捕获到 GeneratorExit
# 尝试在 GeneratorExit 产生后 yield 一个值
# Traceback (most recent call last):
#   File "test.py", line 14, in <module>
#     g.close()
# RuntimeError: generator ignored GeneratorExit
# """


# """
# 一种防止抛出 RuntimeError 的安全生成器写法：设置一个布尔标识。
# """
#
# def safegen():
#     yield 'so far so good'
#     closed = False
#     try:
#         yield 'yay'
#     except GeneratorExit:
#         closed = True
#         raise
#     finally:
#         if not closed:
#             yield 'boo'


# """
# 第四种情况：对已经关闭的生成器对象调用 close() 方法，不会进行任何操作。
# """
# def gen():
#     yield 1
#     print('我不会被执行')
#     print('因为在 yield 1 就抛出了 GeneratorExit 异常')
#     print('未经捕获的 GeneratorExit 异常不会传递')
#     print('返回执行权给 close 的调用方')
#
# g = gen()
# g.close()
# g.close()
# g.close()  # 多次调用 close，什么效果都没有

"""
GeneratorExit 异常只有在生成器对象被激活后，才有可能产生
"""
def gen():
    try:
        yield 1
    except GeneratorExit:
        print('捕获到 GeneratorExit')
        raise
g1 = gen()
next(g1)
g1.close()
"""
捕获到 GeneratorExit
"""

# 没有激活生成器，就不会触发 GeneratorExit 异常
print()
g2 = gen()
g2.close()
print('脚本运行完毕')
"""
脚本运行完毕
"""









