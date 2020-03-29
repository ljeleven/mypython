#__author:"longjin"
#date:  2020/3/29
# -*- coding: UTF-8 -*-
#
import requests

class Common(object):
    def __init__(self):
        self.url_root = 'http://127.0.0.1:12356'

    def get(self, uri, params=''):
        url = self.url_root + uri + params
        res = requests.get(url)
        return res

    def post(self, uri, params=''):
        url = self.url_root + uri
        if len(params) > 0:
            res = requests.post(url, data=params)
        else:
            res = requests.post(url)

        return res