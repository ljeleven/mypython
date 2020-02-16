#__author:"longjin"
#date:  2019/6/24

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 　　　60分以下的用C表示。
# 1.程序分析：(a>b)?a:b这是条件运算符的基本例子
while 1:
    score = int(input('please input your score: '))
    if score < 0:
        print("over")
        break
    elif score < 60:
        print('%d, C'% score)
    elif score < 90:
        print('%d, B'% score)
    else:
        print('%d, A'% score)


