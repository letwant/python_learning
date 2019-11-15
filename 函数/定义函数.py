# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-99))

# 函数参数检查
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operated type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs1(6))


def quadratic(a, b, c):
    ans1 = -b + math.sqrt(pow(b, 2) - 4 * a * c)
    ans2 = -b - math.sqrt(pow(b, 2) - 4 * a * c)
    return ans1/(2 * a), ans2/(2 * a)


a = quadratic(1, 4, 4)
print(a)