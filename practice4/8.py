#__author:"longjin"
#date:  2019/7/2
# -*- coding: UTF-8 -*-
from functools import reduce
# Q1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
L = ['adam', 'LISA', 'barT']
def iii(i):
    return '%s'%(i[:1].upper()+i[1:])
l2 = []
L1 = []
for i in L:
    x = i.lower()
    L1.append(x)

l2 = list(map(iii, L1))

print(l2)

# Q2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def prod(A):
    return reduce(lambda x, y: x*y, A)
print(prod(A))

# Q3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#字符串变换成数字
def char2num(s):
    return DIGITS[s]
#将序列变换成整数
def fn(x, y):
    return x*10 + y

def str2float(s):
    f_before = s.split('.')[0]
    f_after = s.split('.')[1]
    return reduce(fn, map(char2num, f_before))+reduce(fn, map(char2num, f_after))/1000

print(str2float('123.456'))


