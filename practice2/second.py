#__author:"longjin"
#date:  2019/6/9

def bonus(n):
    bonus = 0
    if n <= 100000:
        bonus = n*0.1
    elif 100000 < n <= 200000:
        bonus = 100000*0.1 + (n-100000)*0.075
    elif 200000 < n <= 400000:
        bonus = 100000*0.1 + 100000*0.075 + (n-200000)*0.05
    elif 400000 < n <= 600000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (n-400000)*0.03
    elif 600000 < n <= 1000000:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (n-600000)*0.015
    elif 10000000 < n:
        bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000*0.03 + 400000*0.015 + (n-1000000)*0.01

    return bonus

n = int(input('please input your profit: '))
print(bonus(n))