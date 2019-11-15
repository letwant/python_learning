# -*- coding: utf-8 -*-
# 可以直接作用于for循环的数据类型有以下几种
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function

# 这些可以直接作用于for循环的对象统称为可迭代对象: Iterable对象

# 可以用isinstance()判断一个对象是否是Iterable对象:
from collections import Iterable

value = isinstance([], Iterable)
print(value)  # True
print(isinstance({}, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance((x * x for x in range(10)), Iterable))  # True
print(isinstance(100, Iterable))  # False,因为数字不是可迭代对象

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration
# 错误表示无法继续返回下一个值了

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器: Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象:
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator)) # True
print(isinstance([], Iterator)) # False, list类型不是迭代器
print(isinstance({}, Iterator)) # False, dict类型不是迭代器
print(isinstance('abc', Iterator)) # False, str类型不是迭代器

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

print(isinstance(iter([]), Iterator)) # True
print(isinstance(iter('abc'), Iterator)) # True


'''
为什么list、dict、str等数据类型不是Iterator?

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
知道没有数据时抛出StopIteration错误。可以把这个数据流看作是一个有序序列，但我们却不能提前知道序列的
长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个
数据时它才会计算

Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而使用list是永远不可能存储全体自然数的
'''


'''
小结
凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
集合数据类型如list、dict、str等都是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
'''

# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 5, 8]:
    pass


# 完全等价于:
it = iter([1, 2, 3, 5, 8])
while True:
    try:
        x = next(it)
    except StopIteration as e:
        break