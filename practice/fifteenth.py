#__author:"longjin"
#date:  2019/6/2
import random

def guess():
    b = input('please input the range: ')
    s = random.randint(1,9)
    i = 1
    while i:
        a = int(input('please input a number: '))
        if a > s:
            print('bigger!')
        elif a == s:
            i = 0
            print('equal!')
        elif a < s:
            print('less')

guess()