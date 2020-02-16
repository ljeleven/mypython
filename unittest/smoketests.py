#__author:"longjin"
#date:  2018/8/4
import  unittest
import HTMLTestRunner
import os
from searchtests import SearchTests
from  home_oage_test import HomePageTest

dir = os.getcwd()
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
#home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_tests = unittest.TestSuite(search_tests)
#open the report file
outfile = open(dir + '\smoketestreport.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='test report',
    description='smoke tests'
)
runner.run(smoke_tests)
#unittest.TextTestRunner(verbosity=2).run(smoke_tests)