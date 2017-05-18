# coding=utf-8

import functools


def log(arg):
    if isinstance(arg, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s begin call %s():' % (arg, func.__name__))
                func(*args, **kw)
                print('%s begin call %s():' % (arg, func.__name__))
            return wrapper
        return decorator
    else:
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print('begin call %s():' % arg.__name__)
            arg(*args, **kw)
            print('end call %s():' % arg.__name__)
        return wrapper


@log('execute')
def now():
    print('2017-05-07')


now()