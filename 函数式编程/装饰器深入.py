'''
def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello(something):
    print("hello {}!".format(something))

say_hello('world')
'''

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level = level,
                func = func.__name__
            ))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print("say {}!".format(something))


@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))

if __name__ == '__main__':
    say('hello')
    do('my work')
