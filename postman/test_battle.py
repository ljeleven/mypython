#__author:"longjin"
#date:  2020/3/30
# -*- coding: UTF-8 -*-

from postman import common

def login(comm, username, password):
    uri = '/login'
    payload = 'username=' + username + '&password=' + password
    res = comm.post(uri, payload)
    print(res.text)

def equip(comm, equipid):
    uri = '/selectEq'
    payload = "equipmentid=" + equipid
    res = comm.post(uri, payload)
    print(res.text)

def enemy(comm, enemyid):
    uri = '/kill'
    payload = "enemyid=" + enemyid
    res = comm.post(uri, payload)
    print(res.text)

if __name__ == '__main__':
    comm = common.Common('http://127.0.0.1:12356')
    login(comm, 'criss', 'criss')
    equip(comm, '10001')
    enemy(comm, '20001')

