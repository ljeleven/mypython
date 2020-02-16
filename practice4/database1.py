#__author:"longjin"
#date:  2019/7/16
# -*- coding: UTF-8 -*-

import sys
import pymysql
#建立连接
conn = pymysql.connect(db='test', user='root', passwd='123456', charset='utf8')
cur = conn.cursor()
sql = 'create table a(id int, hh varchar(30));'
cur.execute(sql)
conn.commit()
