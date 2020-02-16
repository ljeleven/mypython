#__author:"longjin"
#date:  2019/6/24

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 1.程序分析：利用while语句,条件为输入的字符不为’\n’
cha = 0
num = 0
no = 0
other = 0
leap = 0

str = input('please input something: ')
for i in str:
    if ord(i) == 13:
        break
    if ord(i) == 32:
        no += 1
    elif 47 < ord(i) < 58:
        num += 1
    elif 64 < ord(i) < 91 or 96 < ord(i) < 123:
        cha += 1
    else:
        other += 1



print('数字:%d,字母:%d, 空格:%d, 其他:%d'% (num, cha, no, other))