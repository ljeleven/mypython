#__author:"longjin"
#date:  2020/3/30
# -*- coding: UTF-8 -*-

from postman import common

comm = common.Common('http://127.0.0.1:12356')
uri = '/selectEq'
equipmentid = '10001'
payload = "equipmentid=" + equipmentid
res = comm.post(uri, payload)
print(res.text)