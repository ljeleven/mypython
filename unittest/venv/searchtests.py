#__author:"longjin"
#date:  2018/7/28
import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    #def setUp(self):#每完成一个测试用例结束都会关闭，然后重新开始
    @classmethod
    def setUpClass(cls):#所有用例共同使用，全部结束后才关闭
        #create a new firefox session
        chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        #navigate to the application home page
        cls.driver.get('https://www.baidu.com/')

    def test_search_by_category(self):
        #get the search textbox
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()

        #enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        #get all the anchor elemens which have producr names displayed
        #currently on result page using find_element_by_xpath method
        products = self.driver.find_elements_by_xpath("//h3[@class='t']/a")
        self.assertEqual(6, len(products))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()
        self.search_field.send_keys('A')
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h3[@class='t']/a")
        for product in products:
            self.assertIn('A', product.text)

    #def tearDown(self):
    @classmethod
    def tearDownClass(cls):
#close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
###verbosity是一个选项,表示测试结果的信息复杂度，有三个值
#0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
#1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”32 (详细模式):测试结果会显示每个测试用例的所有相关的信息
#并且 你在命令行里加入不同的参数可以起到一样的效果
#加入 --quiet 参数 等效于 verbosity=0
#加入--verbose参数等效于 verbosity=2
#什么都不加就是 verbosity=1###