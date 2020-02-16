#__author:"longjin"
#date:  2019/9/15
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.aimporction_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://ww.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()
b = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(b).perform()


a = driver.find_element_by_css_selector('a.setpref')
print(a.text)
a.click()