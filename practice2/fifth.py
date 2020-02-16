#__author:"longjin"
#date:  2019/6/16

def min(x):
    x.sort()
    return x[0]

x =[]
for i in range(3):
    l = int(input('number: '))
    x.append(l)

print(min(x))