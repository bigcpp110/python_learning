

class FibIterator():
    def __init__(self,n):
        self.n=n
        self.current=0
        self.num1=0
        self.num2=1

    def __next__(self):
        if self.current<self.n:
            num=self.num1
            self.num1,self.num2=self.num2,self.num1+self.num2
            self.current+=1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self

