class CountDown():
	def __init__(self,step):
		self.step=step

	def __next__(self):
		if self.step<=0:
			raise StopIteration
		self.step-=1
		return self.step


	def __iter__(self):
		return self


# for element in CountDown(4):
# 	print(element)



class Student():
	def __init__(self):
		self.mylist=[]
		self.count=0

	def add(self,item):
		self.mylist.append(item)	

	def __next__(self):
		self.max_len=len(self.mylist)
		if self.count<self.max_len:
			ret=self.mylist[self.count]
			self.count+=1
			return ret
		else:
			raise StopIteration

	def __iter__(self):
		return self

st=Student()
st.add("小李")
st.add("老王")



def fiba(n):
	a,b=0,1
	i=0
	while i<n:
		yield a,b
		i+=1
		a,b=b,a+b

s=fiba(10)
print(next(s))
print(next(s))
print(next(s))


