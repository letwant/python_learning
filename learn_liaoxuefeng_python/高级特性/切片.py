# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取列表前三个元素？？

# 老办法
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)  # ['Michael', 'Sarah', 'Tracy']

# 使用切片的方法
print(L[0:3])  # ['Michael', 'Sarah', 'Tracy']

# 如果索引是从0开始，可以省略
print(L[:3])  # ['Michael', 'Sarah', 'Tracy']

# 取倒数第一个数
print(L[-1])  # 'Jack'

# 倒数同样支持倒数切片
print(L[-2:])  # ['Bob', 'Jack']

print(L[-2: -1])  # ['Bob']

L = list(range(100))  # 创建一个0到99的数列

# 取前10个数
print(L[: 10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 取后10个数
print(L[-10:])  # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# 前11-20个数
print(L[11: 20])  # [11, 12, 13, 14, 15, 16, 17, 18, 19]

# 前10个数，每两个取一个
print(L[: 10: 2])  # [0, 2, 4, 6, 8]

# 所有数，每5个取一个
print(L[::5])  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 创建一个同样的列表
print(L[:])  # [0, 1, 2, 3, ..., 99]

# tuple也是一个list，唯一的区别是tuple不不可变的，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
T = (0, 1, 2, 3, 4)
print(T[:3])  # (0, 1, 2)

# 字符串也可以看作是一种list，每一个字符代表一个元素，所以字符串也可以用作切片操作
S = 'ABCDEFG'
print(S[2: 5]) # 'CDE'


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

# 答案
def trim(s):
    s_len = len(s)
    if s_len == 0:
        return s
    else:
        while s != '':
            if s[0] == ' ':
                s = s[1: len(s)]
            else:
                break
        while s != '':
            if s[-1] == ' ':
                s = s[-len(s):-1]
            else:
                break
        return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')