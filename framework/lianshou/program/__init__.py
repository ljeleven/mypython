#__author:"longjin"
#date:  2019/8/28
# -*- coding: UTF-8 -*-

import unittest
from lianshou.program.test_hello import TestHello
from lianshou.program.test_fk_math import TestFkMath

test_cases = (TestHello, TestFkMath)
def whole_suite():
    #创建测试加载器
    loader = unittest.TestLoader()
    #创建测试包
    suite = unittest.TestSuite()
    #遍历所有测试类
    for test_class in test_cases:
        #从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(test_class)
        #将测试用例添加到测试包中
        suite.addTest(tests)

    return suite

if __name__ == "__main__":
    with open('report.txt', 'a') as f:
    #创建测试运行器
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(whole_suite())