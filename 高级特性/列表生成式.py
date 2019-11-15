# -*- coding: utf-8 -*-
# 列表生成式即List Comprehensions，是Python内置的非常强大的可以用来创建list的生成式
# 如果想生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = list(range(1, 11))

# 但是如果想生成 [1*1, 2*2, 3*3, 4*4 ... 10* 10] 该怎么做？
# 方法一：使用循环
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 方法二：使用列表生成式
L = [x * x for x in range(1, 11)]
print(L)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面可以加上if判断，给出偶数的平方和
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)  # [4, 16, 36, 64, 100]

# 可以使用两层循环，可以生成全排列
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名，可以通过列表生成式来实现
import os

L = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(L)  # ['切片.py', '列表生成式.py', '生成器.py', '迭代.py', '迭代器.py']

# for循环可以同时使用两个或者多个变量，比如遍历一个dict
d = {'a':1, 'b': 2, 'c': 3, 'd': 4}
for k, v in d.items():
    print(k, '=', v)

# a = 1
# b = 2
# c = 3
# d = 4

# 同理，列表生成式也可以同时使用多个变量
L = [k + '=' + str(v) for k, v in d.items()]
print(L) # ['a=1', 'b=2', 'c=3', 'd=4']

# 练习
# L1 = ['Hello', 'World', 18, 'Apple', None]
# 将L1中的英文单词都变成小写，注意：这个list中既有单词也有数字，要做判断
L1 = ['Hello', 'World', 18, 'Apple', None]
L2= [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 测试通过