#__author:"longjin"
#date:  2019/6/9

def fact(n):
    s = 1
    if n <= 1:
        return s
    else:
        for i in range(1, n+1):
            s = s*i

    return s

n = int(input('please input a number: '))
print('the fact is %d'% fact(n))