#__author:"longjin"
#date:  2018/9/1
import time
from selenium import webdriver
import unittest

class is_enabled_displayed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        cls.driver.get('http://www.baidu.com')

    def test_register_new_user(self):
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        create_acount_button = self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[4]/a')
        try:
            self.assertTrue(create_acount_button.is_enabled() and create_acount_button.is_displayed())
            print('test pass')
        except Exception:
            print('the create acount bottun is not enabeled or displayed')

        create_acount_button.click()
        try:
            self.assertEqual('百度一下，你就知道', self.driver.title)
            print('test pass')
        except Exception:
            print('test failed')

        print(create_acount_button.get_attribute('class'))
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)