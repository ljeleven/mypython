#__author:"longjin"
#date:  2019/6/26
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
# 　　　第10次落地时，共经过多少米？第10次反弹多高？
h = 50
s = [100]
n = int(input('please input a number: '))
for i in range(2, n+1):
    s.append(h*2)
    h = h/2
print(sum(s), h)

Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2

print ('Total of road is %f' % Sn)
print ('The tenth is %f meter' % Hn)
