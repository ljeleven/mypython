#__author:"longjin"
#date:  2018/8/25
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get('http://sahitest.com/demo/index.htm')

    def test_by_id(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
        search_field = self.driver.find_element_by_id('t1')
        try:
            self.assertEqual('128', search_field.get_attribute('maxlength'))
            print('test pass')
            #self.driver.back()
        except Exception:
            print('test failed')
           # self.driver.back()

    def test_switch_to_alert(self):
        self.driver.back()
        #time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()
        #time.sleep(2)
        lert = self.driver.switch_to.alert
        lert.accept()
        #time.sleep(10)

    def test_is_selected(self):
        self.driver.back()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/a[2]').click()
        try:
            select_bottun = self.driver.find_element_by_xpath('//*[@id="c1"]')
            self.assertFalse(select_bottun.is_selected())
            print('test pass 3')
        except Exception:
            print('test fialed 3')

    def test_select(self):
        self.driver.back()
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[4]').click()
        exp_options = ['', 'o1', 'o2', 'o3']

        act_options = []
        select_option = Select(self.driver.find_element_by_id('s1Id'))
        try:
            self.assertEqual(4, len(select_option.options))
            print('test pass 4')
        except Exception:
            print('test failed 4')

        for option in select_option.options:
            act_options.append(option.text)

        try:
            self.assertListEqual(exp_options, act_options)
            print('test pass 5')
        except Exception:
            print('test failed 5, option is not equal')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)