#__author:"longjin"
#date:  2019/6/9
import math
def inte():
    for i in range(10000):
        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))
        if x*x == i+100 and y*y == i+268:
            print(i)


inte()