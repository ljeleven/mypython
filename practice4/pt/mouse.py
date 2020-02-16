#__author:"longjin"
#date:  2019/9/23
# -*- coding: UTF-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="kw"]')
ActionChains(driver).context_click(driver.find_element_by_xpath('//*[@id="kw"]')).perform()