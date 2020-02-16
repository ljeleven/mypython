#__author:"longjin"
#date:  2019/9/23
# -*- coding: UTF-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://blog.csdn.net/jusulysunbeamy/article/details/90003194')
logo = driver.find_element_by_xpath('//*[@id="nav-left-menu"]/li[1]/a/img')
ActionChains(driver).context_click(logo).perform()
time.sleep(3)
pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'down'])
time.sleep(3)
pyautogui.typewrite(['enter'])
time.sleep(4)

driver.quit()