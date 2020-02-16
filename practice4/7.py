#__author:"longjin"
#date:  2019/7/1
# -*- coding: UTF-8 -*-

# 生成器练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
#一层循环
L = []
l = [x*x for x in range(1, 11)]
for i in range(1, 11):
    L.append(i)
print(l, L)
#两层循环
a = []
for m in range(1,4):
    for n in range(5, 9):
        a.append(m+n)

b = [M*N for M in range(1, 4) for N in range(5, 9)]
print(a, b)

#循环加判断
k = []
for kk in range(6):
    if kk < 4:
        k.append(kk*kk)

K = [j*j for j in range(8) if j >4]
print(k, K)


p = ['Hello', 'World', 18, 'Apple', None]
# isinstance(o, str) 判断o是否为字符串，是返回true，不是返回false。
print([o.lower() for o in p if isinstance(o, str)])