# coding=utf-8


import time, threading


balancee = 0


def change_it(n):
    global balancee
    balancee = balancee + n
    balancee = balancee - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balancee)