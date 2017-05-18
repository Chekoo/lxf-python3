# coding=utf-8

from functools import reduce


def prod(L):
    def p(x, y):
        return x * y
    return reduce(p, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))