#__author:"longjin"
#date:  2019/9/24
# -*- coding: UTF-8 -*-



from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/index.htm')
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[4]').click()

s1 = driver.find_element_by_xpath('//*[@id="s1Id"]')
s2 = driver.find_element_by_xpath('//*[@id="s2Id"]')
s3 = driver.find_element_by_xpath('//*[@id="s3Id"]')
s4 = driver.find_element_by_xpath('//*[@id="s4Id"]')
s5 = driver.find_element_by_xpath('//*[@id="s1"]')

print(Select(s1).first_selected_option)
print(Select(s4).all_selected_options)
Select(s3).select_by_index('3')
Select(s2).select_by_value('o2')
Select(s5).select_by_visible_text('Fax')