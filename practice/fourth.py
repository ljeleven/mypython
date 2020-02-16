#__author:"longjin"
#date:  2019/5/26

def times(num, frequency):
    product = 1
    i = 0
    while i < frequency:
        product = product * num
        i = i + 1

    return product

num = int(input('please input the number: '))
frequency = int(input('please input the frequency: '))

print(times(num, frequency))
print(7**4)