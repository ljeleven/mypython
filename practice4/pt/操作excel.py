#__author:"longjin"
#date:  2019/10/7
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import ddt
import unittest
from pt.read_excel import ReadExcel
import os


# curpath = os.path.dirname(os.path.realpath(__file__))
excelpath = r'C:\Users\lj\Desktop\Book1.xls'
data = ReadExcel(excelpath, 'Sheet2')
testdata = data.dict_data()

@ddt.ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(*testdata)
    def test_search(self, data):
        search_content = data['搜索内容']
        self.driver.find_element(By.ID, 'kw').send_keys(search_content)
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        time.sleep(5)
        tt = self.driver.title
        self.assertIn(search_content, tt)
        self.driver.find_element(By.ID, 'kw').clear()

if __name__ == '__main__':
    unittest.main()