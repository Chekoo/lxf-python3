# coding=utf-8


def triangles():
    L = [1]
    for i in range(10):
        yield L
        L = [1] + [L[j] + L[j + 1] for j in range(len(L) - 1)] + [1]


for g in triangles():
    print(g)