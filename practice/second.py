#__author:"longjin"
#date:  2019/5/26

def area(length, width):
    area = length * width
    return area

def perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter

length = float(input("Please input the length: "))
width = float(input("please input the width: "))

print("The area of the rectangle is %f, and the perimeter of it is %f" %(area(length, width), perimeter(length, width)))