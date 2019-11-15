# -*- coding: utf-8 -*-
'''
Python内建的filter()函数用于过滤序列
和map()类似，filter()也接受一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
'''

# 例如在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1  # 这样也可以 ?
# 如果是偶数就返回False，如果是奇数就返回True

print(list(filter(is_odd, [1, 2, 4, 5, 7, 8, 10]))) # [1, 5, 7]


# 把一个序列中的空字符串删掉，可以这么写:
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 's']))) # ['A', 's']

# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数
# 获得所有结果并返回list


# 用filter求素数， 使用的是埃氏筛法
'''
首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
'''

# Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

# 这是一个生成器，并且是一个无限序列

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# 打印100以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break



def foo():
    n = 1
    while True:
        n += 2
        yield n


def foo1(n):
    return lambda x: x%n > 0


def foo2():
    yield 2
    it = foo()
    while True:
        yield next(it)
        it = filter(foo1(n), it)


for n in foo2():
    if n < 100:
        print(n)
    else:
        break





'''
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''

# 第一步：构造一个自然数序列
# 第二步：写筛选函数
# 第三步：生成器





def is_palindrome1(n):
    def dig_iter():  # 构造一个自然数的生成器
        n = 1
        while True:
            yield n
            n += 1

    def sort_func(n):
        str_array = [x for x in str(n)]
        return str_array == str_array[::-1]


    num = dig_iter()
    while True:
        yield next(num)
        num = filter(sort_func, num)



def is_palindrome(n):
    str_array = [x for x in str(n)]
    return str_array == str_array[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')