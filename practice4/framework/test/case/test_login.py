#__author:"longjin"
#date:  2019/10/13
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random
from framework.test.common import myunit, screenshot
from framework.test.page.loginPage import login

class loginTest(myunit.MyTest):
    '''
    测试用户登录
    '''
    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        self.user_login_verify(username='admin', password='123456')
        sleep(3)
        function.insert_img(self.driver, 'user_pwd_true.png')

if __name__ == '__main__':
    unittest.main()