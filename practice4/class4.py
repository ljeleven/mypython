#__author:"longjin"
#date:  2019/7/13
# -*- coding: UTF-8 -*-

"""
定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname) [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
set_info = Setinfo(你要操作的集合)
"""
class Setinfo():
    def __init__(self, sett):
        self.sett = sett

    def add_setinfo(self, keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett.intersection(unioninfo)
            # return self.sett
        return '类型错误'


    def get_union(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett.union(unioninfo)
        return '类型错误'

    def del_difference(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett.difference(unioninfo)

        return '类型错误'


set_info = Setinfo({'c', 'b', 'f', 'd', 'e', 'a'})
print(set_info.add_setinfo('ad'))
print(set_info.get_intersection({'c', 'd', 2}))
print(set_info.get_union({'c', 'd', 2}))
print(set_info.del_difference({'a'}))