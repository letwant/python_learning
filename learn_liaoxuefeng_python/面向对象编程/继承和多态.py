# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()
an = Animal()

print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Cat))


def run_twice(animal):
    animal.run()
    animal.run()


class Itor(object):

    def run(self):
        print('Hello World')


# 只要有run()方法就可以作为参数传进去，鸭子类型
itor = Itor()
run_twice(an)
run_twice(dog)
run_twice(itor)