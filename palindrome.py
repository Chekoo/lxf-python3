# coding=utf-8


def palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(palindrome, range(1000))
print(list(output))