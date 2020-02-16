#__author:"longjin"
#date:  2019/9/25
# -*- coding: UTF-8 -*-


from practice4.pt import opentestpage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

driver = opentestpage.opentest('https://www.baidu.com')
driver.find_element_by_link_text('hao123').click()
driver.find_element_by_link_text('搜狐').click()
aa = driver.window_handles
sleep(5)
driver.switch_to.window(aa[0])
sleep(5)
driver.quit()