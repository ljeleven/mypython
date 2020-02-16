#__author:"longjin"
#date:  2019/7/15
# -*- coding: UTF-8 -*-

def cmp_ignore_case(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1>s2:
        return 1
    if s1<s2:
        return -1
    return 0
a = ['bob', 'about', 'Zoo', 'Credit']


print(sorted(a, key=lambda x:x[0]))
print(a)