# #给类添加方法
# """
# Person.run	=	types.MethodType(run,	None,	Person)
# """
# G	=	(	x*2	for	x	in	range(5))
#
# print(next(G))
# def	gen():
#     i=0
#     while i<5:
#         yield 1
# f=gen()
# print(next(f))
#
# """
# 凡是可作用于	for	循环的对象都是	Iterable	类型；
# 凡是可作用于	next()	函数的对象都是	Iterator	类型
# 集合数据类型如	list	、	dict	、	str	等是	Iterable	但不是	Iterator	，不过可以通过 iter()	函数获得一个	Iterator	对象。
# """
#
# from collections.abc import Iterable
# from collections.abc import Iterator
# print(isinstance(iter([]),	Iterator) )
#
#
# #定义一个函数
# def test(number):
#     #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么称里面 的这个函数为闭包
#     def	test_in(number_in):
#         print("in	test_in	函数,	number_in	is	%d"%number_in)
#         return	number+number_in
#     #其实这里返回的就是闭包的结果
#     return	test_in
# 给test函数赋值，这个20就是给参数number
# ret	=	test(20)
# 注意这里的100其实给参数number_in
# print(ret(100))
# 注意这里的200其实给参数number_in
# print(ret(200))
# a=20
# print(id(a))
# a+=1
# print(id(a))
# a=a+1
# print(id(a))

# import dis
#
# def func1():
#     print("--func1")
#
# def func2():
#     print("func2")
import dis
import time

def deco(f):
    def wrapper():
        start_time = time.time()
        f()
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f():
    print("hello")
    time.sleep(1)
    print("world")

def a():
    print("123")

dis.dis(f)


"""
sys.path.append('/home/itcast/xxx') sys.path.insert(0,	'/home/itcast/xxx')				#可以确保先搜索这个路径
"""
"""
模块重载：
importlib。reload()
"""


"""
Python	使用	LEGB	的顺序来查找一个符号对应的对象
locals	->	enclosing	function	->	globals	->	builtins
"""


"""
is	是比较两个引用是否指向了同一个对象（引用比较）。 ==	是比较两个对象是否相等。
"""