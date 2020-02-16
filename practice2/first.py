#__author:"longjin"
#date:  2019/6/9
def num():
    l1 = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!= j and j != k and i != k:
                    l1.append(i*100+j*10+k)

    print(l1)

num()