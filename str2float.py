# coding=utf-8

from functools import reduce


def inum(x, y):  # 小数部分
    return x * 10 + y


def fnum(x, y):  # 整数部分
    return x * 0.1 + y


def charnum(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
            '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    if s.find('.') == -1:
        return reduce(inum, map(charnum, s))
    return reduce(inum, map(charnum, s[0:s.find('.')])) + \
        reduce(fnum, map(charnum, reversed(s[s.find('.') + 1:]))) * 0.1


print('str2float(\'123.456\') = ',  str2float('123.456'))