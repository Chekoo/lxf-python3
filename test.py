# coding=utf-8

import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float))\
      or not isinstance(c, (int, float)):
        raise TypeError('输入必须是整型或浮点型')
    if a == 0:
        if b != 0:
            r = -c / b
            print('x = ', r)
        else:
            print('无解')
    else:
        D = (b * b - 4 * a * c)
        if D >= 0:
            d = math.sqrt(D)
            x1 = (-b + d) / (2 * a)
            x2 = (-b - d) / (2 * a)
            return x1, x2
        else:
            print('无解')


if __name__ == '__main__':
    a = float(input('input a number: '))
    b = float(input('input a number: '))
    c = float(input('input a number: '))
    print('计算公式为:%dx * x + %dx + %d = 0' % (a, b, c))
    print(quadratic(a, b, c))
