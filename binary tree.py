class Binary_tree():
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

    def insertleft(self,value_left):
        self.left=Binary_tree(value_left)
        return self.left


a = 10
b = 20
c = [a]
a = 15
print(c)
print(id(a))
print(id(c[0]))
print(dir("a"))

