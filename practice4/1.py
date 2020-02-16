#__author:"longjin"
#date:  2019/6/30
# -*- coding: UTF-8 -*-

# 小明的成绩从去年的72分提升到今年的85分，请计算小明成绩提升的百分点。并用
# 字符串格式化显示出'xx.x%'，只保留小数点后一位：

def upgrade(a, b):
    c = b-a
    t = c/a
    print(t)
    return t

per = upgrade(72, 85)*100
#两个连续的%%，则最终会输出一个%号出来，有对%进行转义的含义
print('%.1f%%' % per)