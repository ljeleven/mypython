#__author:"longjin"
#date:  2019/10/7
# -*- coding: UTF-8 -*-
from pt import opentestpage
from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups':0, 'download.default_directory':'E://'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('/html/body/a[1]').click()
sleep(30)
driver.quit()