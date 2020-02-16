# -*- coding:utf8 -*-
#__author:"longjin"
#date:  2019/6/17
import urllib
import urllib.request
import flask


url = 'http://zxreg.speiyou.com/login/ajax_login'
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = 'f379eaf3c831b04de153469d1bec345e'
#对数据进行编码
#data = urllib.urlencode(data)
#如果要是用parse属性就必须加上import request或者加上flask
data = urllib.parse.urlencode(data)
#将数据和url进行连接
request = url+'?'+data
#打开请求获取对象
requestResponse = urllib.request.urlopen(request)
#读取服务端返回的数据
responsestr = requestResponse.read()
#打印数据
responsestr = responsestr.decode('unicode_escape')
print(responsestr)