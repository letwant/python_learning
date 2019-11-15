# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Micheal'
s.age = 12
s.score = 33
print(s.score) # AttributeError: 'Student' object has no attribute 'score'