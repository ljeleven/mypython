#__author:"longjin"
#date:  2019/6/4

def num(n):
    while n:
        print(n)
        n -= 1

n = int(input('please input a number: '))
num(n)