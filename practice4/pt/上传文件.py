#__author:"longjin"
#date:  2019/10/7
# -*- coding: UTF-8 -*-

from pt import opentestpage
from selenium import webdriver
from time import sleep
driver = opentestpage.opentest('http://sahitest.com/demo/php/fileUpload.htm')
bu = driver.find_element_by_xpath('//*[@id="files"]')
bu.send_keys(r'C:\Users\lj\Desktop\Book1.xls')
bu.send_keys(r'C:\Users\lj\Desktop\data.txt')
sleep(3)
driver.find_element_by_xpath('/html/body/form[1]/input[3]').click()