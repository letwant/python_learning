# -*- coding: utf-8 -*-
# 通过字典方式实现
def switch_case(value):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
    }.get(value, 'error')


print(switch_case('a'))


# 通过匿名函数实现
def switch_case(value, x):
    return {
        'a': lambda x: x + 1,
        'b': lambda x: x + 2,
        'c': lambda x: x + 3,
    }[value](x)


print(switch_case('b', 2))



# 通过类实现
# 太麻烦