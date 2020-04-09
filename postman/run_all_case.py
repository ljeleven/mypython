#__author:"longjin"
#date:  2020/4/9
# -*- coding: UTF-8 -*-

import unittest
import os
import HTMLTestRunner
import time
def allcase():
    case_dir = r'E:\python\postman'
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            print(test_case)
            testcase.addTest(test_case)

    return testcase


if __name__ == '__main__':
    report_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
    filepath = os.getcwd() + '\\report\\' + report_name + '.html'
    print(filepath)
    fp = open(filepath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告')
    runner.run(allcase())
    fp.close()
