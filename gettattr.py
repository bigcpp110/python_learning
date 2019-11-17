class People:
    country='China'
    def __init__(self,name):
        self.name=name

    def people_info(self):
        print('%s is xxx' %(self.name))

obj=getattr(People,'country')
print(obj)