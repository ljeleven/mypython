#__author:"longjin"
#date:  2020/3/29
# -*- coding: UTF-8 -*-
#未使用common类-----------------------------------------------
# import requests
# url_login = 'http://127.0.0.1:12356/login'
# username = 'criss'
# password = 'criss'
# payload = 'username='+ username + '&password=' + password
# response_login = requests.post(url_login, data=payload)
# print('response内容： ' + response_login.text)
#--------------------------------------------------------------

#使用common类--------------------------------------------------
from postman import common
comm = common.Common()
uri = '/login'
username = 'criss'
password = 'criss'
params = 'username=' + username + '&password=' + password
res = comm.post(uri, params)
print(res.text)