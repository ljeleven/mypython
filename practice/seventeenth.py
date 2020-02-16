#__author:"longjin"
#date:  2019/6/9

def su(n):
    for i in range(2, n):
        if n%i == 0:
            print('%d is not a prime'% n)
        else:
            print('%d is a prime number. '% n)
        break


a = int(input('please input a number: '))
su(a)