# -*- coding: utf-8 -*-
# 如果给定一个list或tuple，我们可以通过for循环来便利这个list或者tuple，这种遍历方式称为迭代(iteration).

# 在Python中，迭代是通过for...in来完成的，而很多语言比如c语言，迭代list是通过下标完成的。

# 很多数据类型是没有下标的，但是只要是可迭代对象，无论有没有下标，都可以迭代的，比如

d = {'name': 'Job', 'age': 23}

for key in d:
    print(key)

# 如果想迭代value，可以用for value in d.values();
for value in d.values():
    print(value)

# 如果想迭代key和value，可以使用d.items()
for key, value in d.items():
    print(key, value)

# 字符串也是可迭代对象
S = 'ABCD'
for ch in S:
    print(ch)

# 如何判断一个对象是可迭代对象呢
# 可以使用collections模块的iterable类型判断

from collections import Iterable
# 这里报错:  DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is
# deprecated, and in 3.8 it will stop working from collections import Iterable

data = isinstance('abc', Iterable)
print(data)  # True

data = isinstance(123, Iterable)
print(data)  # False


# 如果想遍历list中的下标，Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在
# for循环中同时迭代索引和元素本身

for index, value in enumerate(['A', 'B', 'C', 'D']):
    print(index,': ', value)
# 0 :  A
# 1 :  B
# 2 :  C
# 3 :  D

# 同时引用了两个变量是很常见的
for x, y in[(1, 3), (5, 2), (8, 1)]:
    print(x, y)

# 1 3
# 5 2
# 8 1

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L == []:
       return (None, None)
    else:
        min = max = L[0]
        for item in L: # 多循环了一次，应该使用L[1:]
            if min > item:
                min = item
            if max < item:
                max = item
        return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 测试成功


# 网上更好解法
def foo(L):
    if not L:
        return (None, None)
    else:
        l = b = L[0]
        for k in L[1:]:
            if k < l:
                l = k
            # 这里用 elif 比 if 更好一点
            elif k > b:
                b = k

        return (l, b)