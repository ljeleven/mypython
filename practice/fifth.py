#__author:"longjin"
#date:  2019/5/29

def centigrade(degree):
    return float(5.0/9*(degree-32))

degree = int(input('please input the centigrade: '))
print('%.2f' % centigrade(degree))