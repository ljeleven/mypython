#__author:"longjin"
#date:  2019/7/14
# -*- coding: UTF-8 -*-


import os
import time
import operator

path = 'C:/Users/lj/Desktop/image/'
os.chdir(path)#切换到path目录
cwd = os.getcwd()#获取当前目录


#os.path.getsize(file)获取文件大小
#os.remove(file)删除文件
#os.listdir 发挥指定文件夹包含的文件或文件夹的名字的列表


def createfile(filetype):
    '''根据本地时间创建新文件，如果已存在则不创建'''
    t = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())#将指定格式的当前时间以字符串输出
    newfile = t + '.' + filetype
    if not os.path.exists(newfile):#当前文件是否存在newfile文件
        f = open(newfile, 'w')
        print(newfile)
        f.close()
        print(newfile + ' created')
    else:
        print(newfile + ' already existed.')

def del_zero():
    for file in os.listdir(os.getcwd()):
        if os.path.getsize(file) == 0:
            os.remove(file)
            print(file + ' deleted!')

def del_bysize(size):
    for file in os.listdir(os.getcwd()):
        if os.path.getsize(file) < size:
            os.remove(file)
            print(file + ' deleted!')


hint = '''function:
            1 create new file
            2 delete null file
            3 delete by size
please input number:'''



while True:
    option = input(hint)
    if operator.eq(option, '1'):
        filetype = input('please input file type: ')
        createfile(filetype)
    elif operator.eq(option, '2'):
        del_zero()
    elif operator.eq(option, '3'):
        minsize = int(input('minsize(k): '))
        del_bysize(minsize)
    elif operator.eq(option, 'q'):
        print('quit!')
        break
    else:
        print("disabled input ,please try again....")

