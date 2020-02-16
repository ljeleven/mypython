#__author:"longjin"
#date:  2019/10/7
# -*- coding: UTF-8 -*-

from pt import opentestpage
from time import sleep
from selenium import webdriver

driver = opentestpage.opentest('http://sahitest.com/demo/')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(3)
driver.quit()