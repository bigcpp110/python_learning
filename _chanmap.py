from collections import ChainMap
"""
合并多个字典
"""



a={"x":1,"z":3}
b={"y":2,"z":4}
c=ChainMap(a,b)
# print("x: {}, y: {}, z: {}".format(c["x"], c["y"], c["z"]))
# print(c)



"""
对ChainMap进行修改的时候总是只会对第一个字典进行修改

ChainMap 并不是对源数据的拷贝，而是 指向源数据

"""
# c.pop("z")
# print(c)
# c.pop("y")#不能pop#所以Chainmap是有序的

print("-----------------")
print(c.maps)
print(c.parents)
print(c.parents.maps)
print(c.parents.parents)

c=c.new_child({"a":111})#在前面添加
print(c)

