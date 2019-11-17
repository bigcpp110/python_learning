i=iter("abc")
print(type(i))
print(i.__next__())

print("-"*10+"分割线"+"-"*10)

class Fibs:
    def __init__ (self):
        self.a =0
        self.b =1
    def __next__(self):
        self.a , self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
    	return self

class MyIterator():
	def __init__(self,step):
		self.step=step

	def __next__(self):
		if self.step==0:
			raise StopIteration
		self.step-=1
		return self.step

	def __iter__(self):
		return self

for el in MyIterator(4):
	print(el)


def fibonacci():
	a,b=0,1
	while True:
		yield b
		a,b=b,a+b

print("-"*10+"分割线"+"-"*10)
fib=fibonacci()
print(fib.__next__())

print("-"*10+"分割线"+"-"*10)


import tokenize
reader=open("ennumerate.py","r",encoding='utf-8').__next__

tokens=tokenize.generate_tokens(reader)
print(tokens.__next__())

print("-"*10+"分割线"+"-"*10)

def power(values):
	for value in values:
		print("powering %s"%value)
		va=yield value
		print(va)

def adder(values):
	for value in values:
		print("adding to %s"%value)
		if value % 2==0:
			yield value+3
		else:
			yield value+2

elements=[1,4,7,9,12,19]
res=adder(power(elements))

print("-"*10+"分割线"+"-"*10)


def psychologist():
	print("please tell me your ploblems")
	while True:
		answer=yield 123
		if answer is not None:
			print("abc")
		else:
			print("def")

free=psychologist()
print(free.__next__())
print(free.send("你好"))


print("-"*10+"分割线"+"-"*10)
def my_generator():
	try:
		yield "something"
	except:
		yield "dealing"
	finally:
		print("ok")

gen=my_generator()
print(gen.__next__())
gen.throw(ValueError("mean"))
gen.close()
print(gen.send("123"))#不再报错
print(gen.__next__())#不再报错