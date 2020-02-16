#__author:"longjin"
#date:  2019/6/1

def exchange(a, b):
    t = a
    a = b
    b = t
    print(a, b)

a = int(input('please input a: '))
b = int(input('please input b: '))
exchange(a, b)