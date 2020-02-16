#__author:"longjin"
#date:  2019/9/25
# -*- coding: UTF-8 -*-

from pt import opentestpage
from time import sleep

driver = opentestpage.opentest('http://sahitest.com/demo/index.htm')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[6]').click()
sleep(2)
driver.switch_to.frame(0)
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
sleep(4)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="another"]/iframe'))
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
sleep(5)
driver.quit()
