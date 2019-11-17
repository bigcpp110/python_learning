# def add(*args):
#     return sum(args)
# print(add(1, 2, 3) + 100)
# print(add(5, 5, 5) + 100)

# def add(*args):
#     # 对传入的数值相加后，再加上100返回
#     return sum(args) + 100

# print(add(1, 2, 3))  # 106
# print(add(5, 5, 5))  # 115 

from functools import partial

def add(*args):
    return sum(args)

add_100 = partial(add, 100)
print(add_100(1, 2, 3))  # 106

add_101 = partial(add, 101)
print(add_101(1, 2, 3))  # 107

add_102=partial(add,108)
print(add_102(1,2,3))