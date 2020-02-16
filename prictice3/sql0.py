#__author:"longjin"
#date:  2019/6/28
# -*- coding: UTF-8 -*-
import pymysql
import random
db = pymysql.connect('localhost', 'root', '123456', 'test')
cur = db.cursor()
a = int(input('please input a: '))
b = int(input('please input b: '))
for i in range(200):
    s = random.randint(a, b)
    sql = 'insert into t set RAND = %d' % s
    cur.execute(sql)
    db.commit()

cur.execute('select * from t')
db.commit()
print(cur.fetchall())
db.close()

