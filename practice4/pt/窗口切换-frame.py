#__author:"longjin"
#date:  2019/9/24
# -*- coding: UTF-8 -*-

from pt import opentestpage
from time import sleep

driver = opentestpage.opentest('http://sahitest.com/demo/index.htm')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[5]').click()
sleep(2)
driver.switch_to.frame('top')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[5]').click()
sleep(2)
driver.switch_to.frame(1)
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[5]').click()
sleep(5)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame[2]'))
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[5]').click()
sleep(10)
driver.quit()
