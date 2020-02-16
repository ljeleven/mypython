#__author:"longjin"
#date:  2019/6/2

def footballteam(age, gender):
    a = 0
    if gender in '女' and 10 <= age <= 12:
        a = 1
        print('you can join in our team!')

    return a
i = 0
t = 0
while i<10:
    age = int(input('please tell me your age: '))
    gender = input('please tell me your gender: ')
    a = footballteam(age, gender)
    if a == 1:
        t += 1

    i += 1

print('满足条件的人数为 %d' % t)
