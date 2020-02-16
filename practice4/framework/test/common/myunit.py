#__author:"longjin"
#date:  2019/10/12
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from framework.test.common import browser
class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()