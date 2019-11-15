# -*- coding: utf-8 -*-
from 面向对象编程.继承和多态 import Dog, Animal, Cat

print(type(abs))
# <class 'builtin_function_or_method'>

print(type(123) == type(245))
print(isinstance(123, int))

# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types


def fn():
    pass


# 使用type.FunctionType
print(type(fn) == types.FunctionType)  # True

a = Animal()
d = Dog()
c = Cat()

print(isinstance(d, Animal))  # True
print(isinstance(a, Cat))  # False

print(isinstance((1, 2, 3), (list, tuple)))  # True
print(isinstance([1, 2, 3], (list, tuple)))  # True

# 如果要获得一个对象的所有属性和方法，使用dir()函数，它返回一个包含字符串的list
str = 'ABC'
print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex',
#  'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回本身的长度。在Python中，
# 如果调用len()函数试图获取一个对象的长度，实际上，在len(0函数的内部，它自动去调用该对象的__len__()
# 的方法，所以以下代码是等价的
print(len('ABC'))  # 3
print('ABC'.__len__())  # 3

print('ABC'.lower())  # abc


# 仅仅把属性和方法列出来是不够的，配和getattr()、setattr()、setarrt()以及hasattr()，我们可以直接
# 操作一个对象的状态:

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))  # 有属性'x'吗？  注意属性要用单引号括起来
# True
print(obj.x)
# 9
print(hasattr(obj, 'y'))
# False
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))
# True
print(getattr(obj, 'y'))
# 19
print(obj.y)
# 虽然报没有这个属性，但还是能打印出值
# getattr(obj, 'z') # 试图获取不存在的属性，会报错
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))
# 404

# 也可以获得对象的方法
print(hasattr(obj, 'power'))
# True
print(getattr(obj, 'power'))
# <bound method MyObject.power of <__main__.MyObject object at 0x0000028D9102B9E8>>
fn = getattr(obj, 'power')
print(fn)
# <bound method MyObject.power of <__main__.MyObject object at 0x00000206BE88BA20>>
print(fn())
# 81

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，
# 拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
