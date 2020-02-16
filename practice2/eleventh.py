#__author:"longjin"
#date:  2019/6/22
# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
# 　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 1.程序分析：　兔子的规律为数列1,1,2,3,5,8,13,21….
while 1:
    n = int(input('month: '))
    if n < 3:
        sum = 1
    else:
        sum1 = 1
        sum2 = 1
        sum = 0
        for i in range(2, n):
            sum = sum1 + sum2
            sum1 = sum2
            sum2 = sum

    if n == 0:
        break

    print(sum)