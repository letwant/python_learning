# 关键之处：key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

'''
练习
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0][0]

L2 = sorted(L, key=by_name)
print(L2) # [('Adam', 92), ('Bob', 75), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2) # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]
