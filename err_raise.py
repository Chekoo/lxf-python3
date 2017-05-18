# coding=utf-8


# class FooError(ValueError):
#     pass


# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n


# foo('0')

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' %s)
#     return 10 / n


# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise


# bar()

# im


import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

