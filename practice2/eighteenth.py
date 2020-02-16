#__author:"longjin"
#date:  2019/6/25
# 题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
# 　　　共有5个数相加)，几个数相加有键盘控制。
# 1.程序分析：关键是计算出每一项的值。

a = int(input('please input the number: '))
b = int(input('please input the number: '))
sum = 0
t = 0
for i in range(b):
    sum = sum + a*10**i
    t = sum + t
    print(sum)

print(t)