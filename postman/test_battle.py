#__author:"longjin"
#date:  2020/3/30
# -*- coding: UTF-8 -*-
import unittest

from ddt import ddt, data, unpack

from postman import common



@ddt
class Test_Battle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        comm = common.Common('http://127.0.0.1:12356')
        cls.comm = comm
        print('-----------------------------')

    @data(['criss', 'criss'], ['criss', 'ddt'])
    @unpack
    def test_login(self, username, password):
        uri = '/login'
        payload = 'username=' + username + '&password=' + password
        res = self.comm.post(uri, payload)
        self.assertTrue(res.status_code)

    @data('10001', '10002')
    def test_equip(self, equipid):
        uri = '/selectEq'
        payload = "equipmentid=" + equipid
        res = self.comm.post(uri, payload)
        res.raise_for_status()
        self.assertIn('enemyid', res.text)

    @data('20001', '20002')
    def test_enemy(self, enemyid):
        uri = '/kill'
        payload = "enemyid=" + enemyid
        res = self.comm.post(uri, payload)
        self.assertTrue(res.status_code)

    # @data(['criss', 'criss', '10001', '20001'])
    # @unpack
    # def test_whole(self, username, password, equipid, enemyid):
    #     print(1)
    #     Test_Battle.login(username, password)
    #     Test_Battle.equip(equipid)
    #     Test_Battle.enemy(enemyid)

if __name__ == '__main__':


        # r = BattleTest(comm, username, password, equipid, enemyid)
        # r.test_login('criss', 'criss')
        # r.test_equip('10001')
        # r.test_enemy('20001')
    unittest.main()




        

