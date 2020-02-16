#__author:"longjin"
#date:  2019/6/22

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# # 1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
# # 　　　　　　则表明此数不是素数，反之是素数。
import math
leap = 0
sum = 0
for i in range(101, 201):
    for j in range(2, int(math.sqrt(i+1)+1)):
        if i%j == 0:
            leap = 0
            break
        leap=1

    if leap==1:
        sum += 1
        print(i)

print('the number is %d'% sum)
