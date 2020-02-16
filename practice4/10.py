#__author:"longjin"
#date:  2019/7/3
# -*- coding: UTF-8 -*-

# sort()函数练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
L.sort()
print(L)

# 再按成绩从高到低排序：
def by_name(t):
    return t[1]


L2 = sorted(L, key = by_name, reverse = True)
print(L2)