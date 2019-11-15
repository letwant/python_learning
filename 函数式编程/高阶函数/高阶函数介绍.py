# -*- coding: utf-8 -*-
# 高阶函数英文叫Higher-order function。什么是高阶函数？我们以实际代码为例子，一步一步深入概念。

print(abs(-10)) # 10

print(abs) # <built-in function abs>

# abs(-10)是函数调用，而abs是函数本身

# 函数本身也可以赋值给变量，即：变量可以指向函数
# 如果一个变量指向了一个函数，那么，可以通过该变量来调用这个函数
f = abs
value = f(-10)
print(value) # 10


# 【函数名也是变量】
abs = 10
# abs(-10) # TypeError: 'int' object is not callable


# 【传入函数】
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以就收另一个函数作为参数，
# 这种函数就称之为【高阶函数】

# 【小结】
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式