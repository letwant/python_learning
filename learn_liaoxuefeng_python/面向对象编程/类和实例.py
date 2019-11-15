# -*- coding: utf-8 -*-
class Student(object):
    pass

bart = Student()

class Student(object):
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，
# 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 50)
print(bart.name)

#类中定义的函数第一个参数永远是实例变量self

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{0}: {1}'.format(self.name, self.score))

bart = Student('Bart Simpson', 60)
bart.print_score()

# 给Student类增加新的方法
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{0}: {1}'.format(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print(bart.get_grade())