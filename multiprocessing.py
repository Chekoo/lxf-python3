# coding=utf-8


from multiprocessing import process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')