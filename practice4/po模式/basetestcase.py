#__author:"longjin"
#date:  2019/10/5
# -*- coding: UTF-8 -*-

import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()