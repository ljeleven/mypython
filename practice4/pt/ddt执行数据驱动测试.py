#__author:"longjin"
#date:  2019/10/5
# -*- coding: UTF-8 -*-

from selenium import webdriver
from ddt import ddt, data, unpack
import unittest

@ddt
class searchddt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://www.baidu.com")

    @data('selenium', 'loadrunner', 'jmeter')
    @unpack
    def test_search(self, search_value):
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest(webdriver=2)
