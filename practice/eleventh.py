#__author:"longjin"
#date:  2019/6/2

def leapyear(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print('yes!')
    else:
        print('no!')
while 1:
    year = int(input('please input a year: '))
    leapyear(year)
    print('please input again!')