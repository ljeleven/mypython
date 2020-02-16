#__author:"longjin"
#date:  2019/6/1


def sum(n):
    s = 0
    for i in range(n):
        i += 1
        s = s + i
    return s

n = int(input('please input a number: '))
print(sum(n))
