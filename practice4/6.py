#__author:"longjin"
#date:  2019/6/30
# -*- coding: UTF-8 -*-

# 请定义一个函数quadratic(a, b, c), 接收3个参数，返回一元二次方程 : ax**2+b+c=0
# 的两个解
# 提示：计算平方根可以调用math.sqrt()函数：
#
# 一元二次方程的求根方程：x = (-b±√(b**2−4ac))/2a
import math
def x(a, b, c):
    try:
        t = math.sqrt(b**2 - 4*a*c)
        x1 = (0-b+t)/(2*a)
        x2 = (0-b-t)/(2*a)
        return x1, x2
    except:
        print('无解')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print(x(a, b, c))