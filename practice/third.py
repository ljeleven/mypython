#__author:"longjin"
#date:  2019/5/26

def myfloat(a, b):
    num = a / b
    return round(num)

a = float(input("please input a number:"))
b = float(input("please input another number:"))

print(float(myfloat(a, b)))