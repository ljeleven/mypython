#__author:"longjin"
#date:  2019/10/12
# -*- coding: UTF-8 -*-

from selenium import webdriver
import os
from time import sleep

def insert_img(driver, file_name):
    # base = 'E:\\python\\practice4\\framework\\report\\image\\'
    # file_path = base + file_name
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    base_dir = str(base_dir)
    print(base_dir)
    base_dir = base_dir.replace('\\', '/')
    print(base_dir)
    base = base_dir.split('test_case')[0]
    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_img(driver, 'test_baidu.png')
    # driver.get_screenshot_as_file('E:\\python\\practice4\\framework\\report\\image\\baidu.png')
    sleep(2)
    driver.quit()