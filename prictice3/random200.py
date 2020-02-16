#__author:"longjin"
#date:  2019/6/27

#生成200个指定长度的随机数
a = int(input('please input a range: '))
b = int(input('please input b: '))
s = []
import random
for i in range(200):
    #random.ranuniform(a,b)生成随机的浮点数，random.randint(a,b)生成随机的整数
    n = random.randint(a, b)
    s.append(n)

print(s)