#__author:"longjin"
#date:  2020/2/12
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import prictice3.config

for host, browser in prictice3.config.getconfig().items():
    print(host)
    print(browser)
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities={'platform':'ANY',
                              'browserName':browser,
                              'vwesion':'',
                              'javascriptEnabled':True
                              }
    )
# for host,browser in prictice3.config.getconfig().items():
#     print(host)
#     print(browser)
#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4444/wd/hub",
#         desired_capabilities={
#             'platform':'ANY',
#             'browserName':browser,
#             'vwesion':'',
#             'javascriptEnabled':True
#         }
#     )
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys("hello")
    driver.find_element_by_id('su').click()
    time.sleep(5)
    driver.quit()







# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time
# import prictice3.config
#
# for host,browser in prictice3.config.getconfig().items():
#     print(host)
#     print(browser)
#     driver = webdriver.Remote(
#         command_executor="http://127.0.0.1:4444/wd/hub",
#         desired_capabilities={'platform':'ANY',
#                               'browserName':browser,
#                               'vwesion':'',
#                               'javascriptEnabled':True
#                               }
#     )
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys("hello")
#     driver.find_element_by_id("su").click()
#     time.sleep(3)
#     driver.quit()