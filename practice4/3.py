#__author:"longjin"
#date:  2019/6/30
# -*- coding: UTF-8 -*-

h = float(input('please input your height: '))
w = float(input('please input your weight: '))
def BIM(h, w):
    return w/h**2

if BIM(h, w) < 18.5:
    print('you are underweight! ')
elif 18.5 <= BIM(h, w) <25:
    print('your weight is normal.')
elif 25 <= BIM(h, w) < 28:
    print('you are overweight!')
elif 28 <= BIM(h, w) < 32:
    print('you are fat!')
elif 32 <= BIM(h, w):
    print('you are too heavy!!!')


