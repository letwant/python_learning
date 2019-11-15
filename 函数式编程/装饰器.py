def now():
    print('2015-12-3')

f = now
f()

print(now.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-12-3')

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s:' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-12-3')

now()

print(now.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log(text):
    def decotator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decotator

'''
练习
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
import time

def exec_time(func):
    exec = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call {0}() at {1}'.format(func.__name__, exec))
        return func(*args, **kw)
    return wrapper

@exec_time
def log():
    print('hello world!')

log()