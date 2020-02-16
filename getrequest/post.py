#__author:"longjin"
#date:  2019/6/18
# -*- coding:utf8 -*-
import urllib
from urllib.request import Request

url = 'http://xapi.kybyun.com/user/login'
data = {}
data['appchg'] = 'Appstore'
data['apptype'] = '21'
data['appver'] = '2.1.3.1'
data['email'] = 'mushishi01'
data['isbind'] = '0'
data['passwd'] = '111111'
data['sysdev'] = 'iPhone 6 Plus'
data['sysver'] = '9.3'
data['uuid'] = '6ff7553bd47c8077905c3920bc0d8b3'
#数据编码及赋值
data = urllib.parse.urlencode(data)
req = Request(url, data)
#打开地址
reqr = urllib.request.urlopen(req)
#读取获得的值
reqr = reqr.read()
#打印
print(reqr)

