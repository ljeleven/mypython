#__author:"longjin"
#date:  2019/7/10
# -*- coding: UTF-8 -*-

"""
三、定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname) [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	[list:列表类型]
4 删除并且返回最后一个元素：del_key()

a = Listinfo([44,222,111,333,454,'sss','333'])
"""
class Listinfo():
    def __init__(self, list):
        self.list = list

    def add_key(self, keyname):
        if isinstance(keyname, (str, int)):
            self.list.append(keyname)
            return self.list

    def get_key(self, num):
        if num > 0 and num < len(self.list):
            return self.list[num]

        return '超出取值范围'

    def update_list(self, list2):
        if isinstance(list2, list):
            self.list.extend(list2)
            return self.list

        return '类型错误'

    def del_key(self):
        a = self.list.pop(-1)
        return self.list

a = Listinfo([44,222,111,333,454,'sss','333'])

print(a.add_key(1))
print(a.get_key(1))
print(a.update_list([1, 2, 3]))
print(a.del_key())