# coding=utf-8


# 编写一个程序，能在当前目录及当期目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os


def dir_l():
    return [x.lower() for x in os.listdir('.')]