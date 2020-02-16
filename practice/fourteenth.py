#__author:"longjin"
#date:  2019/6/2

def split(cost, n):
    price = (cost + cost*0.15)/n
    return price

cost  = float(input('please input the cost: '))
n  = float(input('please input the number of persons: '))
print('you should pay %f per person.' % split(cost, n))