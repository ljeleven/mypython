#__author:"longjin"
#date:  2019/6/15

def whichday(year, month, day):
    days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    sum = 0

    sum = days[month - 1] + day

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month > 2:
            sum = sum + 1

    return sum

year = int(input("year: "))
month = int(input('month:'))
day = int(input('day: '))
print(whichday(year, month, day))