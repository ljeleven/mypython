#__author:"longjin"
#date:  2019/10/13
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from framework.test.page.base import Base_Page
from time import sleep


class login(Base_Page):
    '''
    禅道登录
    '''

    url = '/'
    login_username_loc = (By.ID, 'acount')
    login_passwd_loc = (By.NAME, 'password')
    login_button_loc = (By.ID, 'submit')
    login_error_loc = (By.CSS_SELECTOR, 'head > script:nth-child(3)')

    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_passwd_loc).clear()
        self.find_element(*self.login_passwd_loc).send_keys(password)

    def login_button(self):
        self.find_element(self.login_button_loc).click()


    def user_login(self, username="admin", password='123456'):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    def login_error_hint(self):
        self.switch_frame('hiddenwin')
        return self.fine_element(*self.login_error_loc).text




