#__author:"longjin"
#date:  2020/3/29
# -*- coding: UTF-8 -*-
# 未使用common类----------------------------------
# import requests
# url_index = 'http://127.0.0.1:12356/'
# response_index = requests.get(url_index)
# print('Response内容： '+response_index.text)
#--------------------------------------------------

#使用common类--------------------------------------
from postman import common
comm = common.Common()
uri = '/'
res = comm.get(uri)
print(res.text)
#--------------------------------------------------