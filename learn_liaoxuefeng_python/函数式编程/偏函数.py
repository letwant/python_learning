# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
import functools

print(int('12345', base=8))
print(int('12345', base=16))

def int2(x, base=2):
    return int(x, base)

print(int2('10100010'))

int3 = functools.partial(int, base=2)
print(int3('10111011'))
