#__author:"longjin"
#date:  2019/7/31
# -*- coding: UTF-8 -*-


from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
# 去掉"Chrome正受到自动测试软件的控制。"
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
dri = webdriver.Chrome(chrome_options=options)

dri.get('https://www.baidu.com')
dri.maximize_window()
dri.implicitly_wait(10)
# aa = dri.find_element_by_id("kw")
# print(aa.size)
# print(dri.find_element_by_xpath('//*[@id="jgwab"]').text)
# time.sleep(5)
# dri.get('https://www.cnblogs.com/captainmeng/p/7845695.html')
# time.sleep(4)
# print(dri.find_element_by_xpath('//*[@id="mainContent"]/div').get_attribute('class'))
# time.sleep(4)
# dri.back()
# print(dri.find_element_by_xpath('//*[@id="su"]').get_attribute('type'))
# time.sleep(5)
# print(dri.find_element_by_xpath('//*[@id="kw"]').is_displayed())
# time.sleep(5)
# oo = dri.find_element_by_xpath('//*[@id="su"]')
#ActionChains的操作一定要加perform()
# ActionChains(dri).context_click(oo).perform()
# time.sleep(3)
# ActionChains(dri).double_click(dri.find_element_by_xpath('//*[@id="u1"]/a[8]')).perform()



#对键盘的操作
from selenium.webdriver.common.keys import Keys
# dri.find_element_by_id('kw').send_keys('自动化')
# dri.find_element_by_id('su').click()
# time.sleep(5)
# dri.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
# time.sleep(2)
# dri.find_element_by_id('su').click()
# time.sleep(5)
# dri.find_element_by_id('kw').clear()
# dri.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# time.sleep(1)
# dri.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
# time.sleep(1)
# dri.find_element_by_id('kw').send_keys('hhh')
# time.sleep(1)
# dri.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
# time.sleep(2)
# dri.find_element_by_id('kw').send_keys(Keys.ENTER)
# time.sleep(2)
# #获取一组对象
# li = dri.find_elements_by_class_name('mnav')
# li[0].click()
# print(dri.title)
# print(dri.current_url)


# https://www.cnblogs.com/captainmeng/p/7902729.html
#切换窗口
# win = dri.current_window_handle
#
# js = "window.open('https://www.cnblogs.com/captainmeng/p/7902729.html')"
# dri.execute_script(js)
# time.sleep(3)
# all_win = dri.window_handles
#
# print(win)
# print(all_win)


#鼠标移动到设置
ActionChains(dri).move_to_element(dri.find_element_by_xpath('//*[@id="u1"]/a[8]')).perform()
time.sleep(2)
dri.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[2]').click()
time.sleep(5)
dri.find_element_by_xpath('//*[@id="adv-setting-4"]/select').click()
time.sleep(2)
dri.find_element_by_xpath('//*[@id="adv-setting-4"]/select/option[3]').click()
time.sleep(10)
dri.quit()