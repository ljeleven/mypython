#__author:"longjin"
#date:  2019/7/10
# -*- coding: UTF-8 -*-

a = {'1': '2', '3': '4', '5': '6'}
b = {'11': '22', '3': '44', '55': '66'}
#方法1：dict(a.items()+b.items())
# print(dict(list(b.items()) + list(a.items())))
b.update(a)
print(b)
print(dict(a, **b))