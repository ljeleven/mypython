#__author:"longjin"
#date:  2019/5/26

def abcd(a, b, c, d):
    t = c * d
    num = a + b - t
    return num

a = int(input("Please input a number: "))
b = int(input("Please input a number: "))
c = int(input("Please input a number: "))
d = int(input("Please input a number: "))

print(abcd(a, b, c, d))