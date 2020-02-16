#__author:"longjin"
#date:  2019/7/8
# -*- coding: UTF-8 -*-
"""
二、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
"""
class dictclass():
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        del self.dict[key]
        return self.dict

    def get_dict(self, key):
        if key in self.dict.keys():
            return self.dict[key]

        return 'not found'

    def get_key(self):
        return list(self.dict.keys())

    def update_dict(self, a):
        self.dict.update(a)
        l = []
        print(self.dict)
        for i in self.dict.keys():
            l.append(self.dict[i])

        return l



a = dictclass({"姓名": "张三", "年龄": "18", "性别": "男"})


print(a.del_dict('性别'))
print(a.get_dict('姓名'))
print(a.get_key())
print(a.update_dict({'gender': 'fale'}))
