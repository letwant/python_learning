# -*- coding: utf-8 -*-
# 背景：如果生成一个很大的列表，全部加载在内存里是不可取的，可以通过一个方法生成一个列表，需要其中
# 的某些元素后只要获取到就可以了，级列表元素可以按照某种算法推算出来。
# Python中，这种一边循环一边计算的机制，成为生成器，generator

#要创建一个generator，有很多种方法。
#第一种方法，把一个列表生成式的[]改成()就可以创建一个generator
L = [x * x for x in range(10)]
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

L = (x * x for x in range(10))
print(L) # <generator object <genexpr> at 0x0000013A797C36D8>

# 如何打印出generator中的每一个元素呢

# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
value = next(L)
print(value) # 0
print(next(L)) # 1
print(next(L)) # 4

# 可以通过for循环来迭代generotor，因为generator也是可迭代对象：
g = (x * x for x in range(10))
for n in g:
    print(n)

# Fibonacci（费波拉契数列），用函数打印出来
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

print(fib(6))

# fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(f) # <generator object fib at 0x00000120DC4A37C8>

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行然后语句就返回，
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句就返回，再次执行时从上次返回的
# yield语句处继续执行
# 定义一个generator，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield  5

o = odd()
print(next(o))
# step 1
# 1
print(next(o))
# step 2
# 3
print(next(o))
# step 3
# 5

# 可以用for...in来遍历yield的函数
for n in fib(6):
    print(n)
# 1
# 1
# 2
# 3
# 5
# 8
# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
# 必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value', e.value)
        break

# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value done

# 练习
"""
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
"""

# 网上优秀代码，自己想不出来
def triangles():
    a = [1]
    while 1:
        yield a
        a = [x + y for x, y in zip(a + [0], [0] + a)]


# 网上能看的懂的代码
def triangles1():
    L = [0, 1, 0]
    yield [1]
    while True:
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
        yield L
        L = [0] + L + [0]

# 其中[0 + [1] = [1, 2]
# 测试

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')