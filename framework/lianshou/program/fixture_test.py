#__author:"longjin"
#date:  2019/9/2
# -*- coding: UTF-8 -*-
import unittest
from lianshou.testtest.hello import *

class TestHello(unittest.TestCase):
    # 测试say_hello函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), 'hello world')

    # @unittest.skip('临时跳过test_add')
    def test_add(self):
        self.skipTest('pass')
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-1, 0), -1)

    @classmethod
    def setUpClass(cls):
        print('_______________________________')

    @classmethod
    def tearDownClass(cls):
        print("___________end_________________")