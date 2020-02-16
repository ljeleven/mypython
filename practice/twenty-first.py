#__author:"longjin"
#date:  2019/6/9
def hcf(m, n):
    mid = 0
    if m >= n:
        mid = n
    else:
        mid = m
    hcf = 1
    for i in range(1, int(mid)+1):
        if m%i == 0 and n%i == 0:
            hcf = i

    return hcf
m = int(input('m: '))
n = int(input('n: '))
print(hcf(m, n))
