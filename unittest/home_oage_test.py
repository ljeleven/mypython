#__author:"longjin"
#date:  2018/8/4
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new firefox session
        chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://www.baidu.com/')

    def test_search_field(self):
        #check search field exists on home page
        self.assertTrue(self.is_element_present(By.NAME, 'wd'))

    def test_language_option(self):
        # check the language option dropdown on home page
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def test_shopping_cart_empty_message(self):
        # check content of my shopping cart block on home page
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')
        shopping_cart_icon.click()
        shopping_cart_status = self.driver.find_element_by_css_selector('p.empty').text
        self.assertEqual('you have no items in your shopping cart.', shopping_cart_status)

        close_button = self.driver.find_element_by_css_selector('div.minicart-wrapper a.close')
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        #close the browser window
        cls.driver.quit()

    def is_element_present(self, how , what):
        try:
            self.driver.find_element(by = how, value = what)
        except :
            NoSuchElementException
            return False
        return True

if __name__ == "__main":
    unittest.main(verbosity=2)