#__author:"longjin"
#date:  2019/10/5
# -*- coding: UTF-8 -*-
from abc import abstractmethod
from abc import abstractclassmethod

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


    @abstractmethod
    def _validate_page(self, driver):
        return

    @property
    def search(self):
        from search import  SearchRegion
        return SearchRegion(self.driver)


class InvalidPageException(Exception):
    pass
