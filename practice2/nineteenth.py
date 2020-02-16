#__author:"longjin"
#date:  2019/6/25
# 题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
# 　　　找出1000以内的所有完数。
# 1. 程序分析：请参照程序<–上页程序14.
l = []
s = []
for n in range(1000):
    sum = 0
    for i in range(1, n+1):
        while n != i:
            if n%i == 0:
                l.append(i)
                n = n/i
            else:
                break
        for j in range(len(l)):
            sum = sum + l[j]

        if sum == n:
            s.append(n)

print(s)