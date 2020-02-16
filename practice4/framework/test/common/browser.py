#__author:"longjin"
#date:  2019/10/12
# -*- coding: UTF-8 -*-
#封装打开浏览器的操作
from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    dri = browser()
    dri.get('https://baidu.com')
    dri.quit()

