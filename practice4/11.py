#__author:"longjin"
#date:  2019/7/4
# -*- coding: UTF-8 -*-
#
# 请编写一个decorator， 能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
def sum():
    # s = 0
    # for i in n:
    #     s = s + n
    #
    # return s
    print('8')
    print('4wdfsdf')
    print('dfgdf')
    print('sfskdjw3')


def dec(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('begin call')
        func(*args, **kwargs)
        print('end call')

        return
    return inner

@dec
def cc():
    return 2


a = dec(sum)
a()
b = dec(cc)
b()
cc()

@dec
def two(a, b, *args):
    print(a, b, args)

two(1, 2, 3, 4)









