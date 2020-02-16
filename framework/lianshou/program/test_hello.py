#__author:"longjin"
#date:  2019/8/28
# -*- coding: UTF-8 -*-

import unittest
from lianshou.testtest import hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(hello.say_hello(), 'hello world')

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(0, 4), 4)
        self.assertEqual(hello.add(-1, 3), 2)
