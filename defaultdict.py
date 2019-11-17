

# import collections
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# a="123"
# d = collections.defaultdict(int)
# print(d)
# d.update([123])
# print(d.values())
# for k, v in s:#元组拆包
#     d[k].append(v)
# print(d.pop("yellow"))
#
#
# print(list(d.items()))

# from collections import defaultdict
# my_dict = {}
# # 使用int作为defaultdict的default_factory
# # 将key不存在时，将会返回int()函数的返回值
# my_defaultdict = defaultdict(int)
# print(my_defaultdict['a']) # 0
# print(my_dict.get("a"))
# print(int())
s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
d = {}
for k, v in s:
    # setdefault()方法用于获取指定key对应的value.
    # 如果该key不存在，则先将该key对应的value设置为默认值:[]
    d.setdefault(k, []).append(v)
print(list(d.items()))