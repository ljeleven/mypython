#__author:"longjin"
#date:  2020/3/3
# -*- coding: UTF-8 -*-

import requests
import unittest

class V2exAPITestCase(unittest.TestCase):
    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {"name": "php"}
        for node_name in ['php', 'python', 'qna']:
            #数据驱动
        # hearders = {
        #     'cache-contro': "no-cache",
        #     'postman-token': "fac2974f-ac28-93f8-a52d-131696879ed3"
        # }

        # responce = requests.request("GET", url, hearders=hearders, params=querystring)
            responce = requests.request("GET", url, params={'name': node_name}).json()
            self.assertEqual(responce['name'], node_name)
        # print(responce.text)

    if __name__ == '__main__':
        unittest.main()