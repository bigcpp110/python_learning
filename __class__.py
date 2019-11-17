class Test:
    def prt(self):
        print(self)
        print(self.__class__)
class B(Test):
	pass
 
t = B()
t.prt()
