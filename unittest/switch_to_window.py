#__author:"longjin"
#date:  2018/8/11
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.maximize_window()
#获得百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.get('http://www.baidu.com')
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now register window')
        driver.find_element_by_name('userName').send_keys('hhhhh8888888hh')
        driver.find_element_by_name('password').send_keys('abcdef1ddd')
        time.sleep(10)


driver.quit()