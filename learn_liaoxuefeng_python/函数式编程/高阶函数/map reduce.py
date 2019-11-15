# -*- coding: utf-8 -*-

'''
Python内建了map()和reduce()函数
【map函数】 map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用于序列的每个元素，
并把结果作为新的Iterator返回
'''


# 举例说明，如果我们有一个函数f(x) = x ^2，要把这个函数作用到一个list中[1, 2, 3, 4, 5, 6, 7]上，就可以用到map()

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

# 把刚才的这个list中的每个元素转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))  # ['1', '2', '3', '4', '5', '6', '7']


def str_lower(x):
    if isinstance(x, str):
        s = x.lower()
        return s
    return x


L = ['Hello', 'World', 23, None]

lis = list(map(str_lower, L))
print(lis)

# 【teduce的用法】: reduce把一个函数作用在一个序列[x1, x2, x3,...]上，这个函数必须接受两个参数
# reduce把结果继续和序列的下一个元素做累积计算，其效果是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比如对一个序列求和
from functools import reduce


def add(x, y):
    return x + y


value = reduce(add, [1, 3, 5, 9, 10])
print(value)  # 28


# 如果要把序列[1, 3, 5, 7, 9]变成13579，可以用reduce实现
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9, ]))  # 13579

# 配合map()，我们可以写出把str转为int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('123456'))  # 123456


# 可以利用lambda函数进一步简化

def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('654321'))  # 654321

'''
练习
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    def str_lower(s):
        x = s.lower()
        head = x[0]
        return head.upper() + x[1:]

    return str_lower(name)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)  # ['Adam', 'Lisa', 'Bart']

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    def mul(x, y):
        return x * y
    return reduce(mul, L)

'''
网上更优解法：
def prod(L):
    reduce(lambda x, y: x * y, L)
'''

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    arr = s.split('.')
    integer = arr[0]
    decimal = arr[1]
    def decimal2float(decimal):
        sum, mul = 0, 10
        for str in decimal:
            sum += int(str) / mul
            mul *= 10
        return sum
    return int(integer) + decimal2float(decimal)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

'''
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for i in range(len(s)):
        if s[i] == ".":
            length1 = i
    s = s[0:length1] + s[(length1+1):]
    x = reduce(lambda x, y: x  10 + y, map(lambda x: DIGITS[x], s))
    y = len(s) - length1
    return x / (10 * y)
'''