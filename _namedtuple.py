"""
namedtuple

namedtuple是一个 工厂函数，定义在python标准库的collections模块中，使用此函数可以创建一个可读性更强的元组

namedtuple函数所创建（返回）的是一个 元组的子类（python中基本数据类型都是类，且可以在buildins模块中找到）

namedtuple函数所创建元组，中文名称为 具名元组

在使用普通元组的时候，我们只能通过index来访问元组中的某个数据

使用具名元组，我们既可以使用index来访问，也可以使用具名元组中每个字段的名称来访问

值得注意的是，具名元组和普通元组所需要的内存空间相同，所以 不必使用性能来权衡是否使用具名元组

"""


"""
参数
def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):

"""

"""
有两个必填参数typename和field_names

"""
"""
typename

参数类型为字符串
具名元组返回一个元组子对象，我们要为这个对象命名，传入typename参数即可

"""
"""
field_names

参数类型为字符串序列
用于为创建的元组的每个元素命名，可以传入像['a', 'b']这样的序列，也可以传入'a b'或'a, b'这种被逗号或空格分割的单字符串
必须是合法的标识符。不能是关键字如class,def等
"""

"""
rename

注意的参数中使用了*，其后的所有参数必须指定关键字
参数为布尔值
默认为False。当我们指定为True时，如果定义field_names参数时，出现非法参数时，会将其替换为位置名称。如['abc', 'def', 'ghi', 'abc']会被替换为['abc', '_1', 'ghi', '_3']
"""

"""
defaults
参数为None或者可迭代对象
当此参数为None时，创建具名元组的实例时，必须要根据field_names传递指定数量的参数
当设置defaults时，我们就为具名元组的元素赋予了默认值，被赋予默认值的元素在实例化的时候可以不传入
当defaults传入的序列长度和field_names不一致时，函数默认会右侧优先
如果field_names是['x', 'y', 'z']，defaults是(1, 2)，那么x是实例化必填参数，y默认为1，z默认为2
"""
from collections import namedtuple


Point=namedtuple("Point",["x","y"])
p=Point(11,y=22)
ret1=p[0]+p[1]
print("p[0]+p[1]",ret1)
x,y=p
print("x,y:",x,y)
print("p.x,p.y:",(p.x+p.y))
print("P:",p)




"""
特性

"""
print("*"*20)


# _make(iterable)
t = [11, 22]
print(Point._make(t))

#_asdict()
p = Point(x=11, y=22)
print(p._asdict())

#_replace(**kwargs)
print(p._replace(x=33))

#_fields
print(p._fields)
Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))


#_fields_defaults
Account = namedtuple('Account', ['type', 'balance',"age"], defaults=[1,2])#defaults 设置默认值，默认值先给后一个
print(Account._fields_defaults)
print(Account('premium',123))# 像赋值
print(Account._fields_defaults)


"""
使用技巧
"""
print("---使用技巧---")
print(getattr(p,"x"))
d = {'x': 11, 'y': 22}
print(Point(**d))

class Point(namedtuple('Point', ['x', 'y'])):
	__slots__ = ()
	@property
	def hypot(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5
	def __str__(self):
		return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

print("-----------类--------------")
for p in Point(3, 4), Point(14, 5/7):
	print(p)#打印对象
	print(type(p))

"""
纸牌
"""
Card = namedtuple('Card', 'rank suit')

class FrenchDeck:
    # 等级2-A
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # 花色红黑方草
    suits = 'spades diamonds clubs hearts'.split()
    # 构建纸牌
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    # 获取纸牌
    def __getitem__(self, position):
        return self._cards[position]

print("--------纸牌-----------")
from random import randint
french_deck = FrenchDeck()
print(french_deck[randint(0,52)])
print(french_deck[randint(0,52)].rank)
print(french_deck[randint(0,52)].suit)