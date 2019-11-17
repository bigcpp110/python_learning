class WithDecorators:
	@staticmethod
	def some_static_method():
		print("this is a static method")
	@classmethod
	def some_class_method(cls):
		print("this is a class method")


"""
函数装饰器
"""
def mydecorator(func):
	def wrapped(*args,**kwargs):
		result=func(*args,**kwargs)
		return result
	return wrapped

"""
类装饰器
"""
class DecoratorAsClass:
	def __init__(self,func):
		self.func=func

	def __call__(self,*args,**kwargs):
		result=self.func(*args,**kwargs)
		return result

"""
参数化装饰器
"""
def repeat(number=3):
	# print("装饰有参数")
	def actual_decorator(func):
		# print("开始装饰")
		def wrapped(*args,**kwargs):
			result=None
			for _ in range(number):
				result=func(*args,**kwargs)
			return result
		return wrapped
	return actual_decorator

@repeat(2)
def foo():
	print("foo")

# foo()


def dummy_decorator(func):
	def wrapped(*args,**kwargs):
		return func(*args,**kwargs)
	return wrapped

@dummy_decorator
def func_with_important_docstring():
	"""这是我们想要保存重要文档的字符串."""
	pass

print(func_with_important_docstring.__name__)
print(func_with_important_docstring.__doc__)

from functools import wraps
def dummy_decorator(func):
	@wraps(func)
	def wrapped(*args,**kwargs):
		return func(*args,**kwargs)
	return wrapped

@dummy_decorator
def func_with_important_docstring():
	"""这是我们想要保存重要文档的字符串."""
	pass

print(func_with_important_docstring.__name__)
print(func_with_important_docstring.__doc__)


"""
参数检查
"""
# print("----------参数检查-----------")


# rpc_info={}
# def xmlrpc(in_=(),out=(type(None),)):
# 	def _xmlrpc(func):
# 		func_name=func.__name__
# 		rpc_info[func_name]=(in_,out)
# 		def _check_types(elements,types):
# 			if len(elements)!=len(types):
# 				raise TypeError("argument count is wrong")
# 			typed=enumerate(zip(elements,types))
# 			for index,couple in typed:
# 				arg,of_the_right_type=couple
# 				if isinstance(arg,of_the_right_type):
# 					continue
# 				raise TypeError(
# 					"arg #%d should be %s"%(index,of_the_right_type))
# 		def __xmlrpc(*args):
# 			checkable_args=args[1:]
# 			_check_types(checkable_args,in_)
# 			res=func(*args)
# 			if not type(res) in (tuple,list):
# 				checkable_res=(res,)
# 			else:
# 				checkable_res=res
# 			_check_types(checkable_res,out)
# 			return res
# 		return __xmlrpc
# 	return _xmlrpc

# class RPCView:
# 	@xmlrpc((int,int))
# 	def methl(self,int1,int2):
# 		print("received %d and %d"%(int1,int2))

# 	@xmlrpc((str,),(int,))
# 	def meth2(self,phrase):
# 		print("received %s"%phrase)
# 		return 12
# print(rpc_info)
# my=RPCView()
# my.methl(1,2)
# my.meth2(2)







"""
上下文
"""
# from threading import RLock
# lock=RLock()
# def synchronized(func):
# 	def _synchronized(*args,**kwargs):
# 		lock.acquire()
# 		try:
# 			func(*args,**kwargs)
# 		finally:
# 			lock.release()
# 			return _synchronized


# @synchronized
# def thread_safe():
# 	pass

# thread_safe()