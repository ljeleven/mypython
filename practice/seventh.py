#__author:"longjin"
#date:  2019/6/1

def num(n):
    if n%3 == 0 and n%5 == 0:
        print('yes')
    else:
        print('no!')

while 1:
    n =  int(input('please input a number: '))
    num(n)
    print('input again')