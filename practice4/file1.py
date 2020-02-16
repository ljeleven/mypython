#__author:"longjin"
#date:  2019/7/14
# -*- coding: UTF-8 -*-

'''把一个数字的list从小到大排序，然后写入文件，然后从文件中读取出来文件内容，然后反序，在追加到文件的下一行'''
import random
import os
import time

l = []
for i in range(20):
    l.append(random.randint(0, 100))


l.sort()
t = ','.join(list(map(str, l)))
print(l)
path = 'C:/Users/lj/Desktop/image/'
os.chdir(path)
os.getcwd()
file = time.strftime('%H-%M-%S', time.localtime()) + '.txt'
if not os.path.exists(file):
    f = open(file, 'w')
    for i in t:
        f.write(i)
    f.close()
else:
    print(file + ' existed!')

o = open(file, 'r+')
k = o.read()
t = k.split(',')
t.sort(reverse=-1)
txt2 = ','.join(list(map(str, t)))
o.write(txt2)
o.close()
print(t)

ll = ('4', '63', '456')
lll = ','.join(ll)#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
print(lll)