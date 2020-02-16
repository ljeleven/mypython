#__author:"longjin"
#date:  2019/7/3
# -*- coding: UTF-8 -*-

# 回数是指从左向右读和从右向左读都是一样的数，例如12321,909。请利用filter()滤掉非回数：
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
def times(x):
    a, b, c = x, 0, 0
    while a:
        b = a%10
        c = c*10 + b
        a = a//10 #//返回整数部分，抛弃余数

    if c == x:
        return True

print(list(filter(times, range(1, 1000))))