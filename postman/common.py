#__author:"longjin"
#date:  2020/3/29
# -*- coding: UTF-8 -*-
#
import requests

class Common(object):
    def __init__(self, url_root):
        self.url_root = url_root

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