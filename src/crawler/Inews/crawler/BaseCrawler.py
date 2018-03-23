'''
    Title : BaseCrawler.py
    Author : ngh
'''

'''
    import list
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

from time import sleep
from random import random


'''
    Class : BaseCrawler
    Description : Parent class for all crawlers
'''
class BaseCrawler:
    def __init__(self, url):
        self.url = url
        self.heads = []
        self.bodys = []

        # self._loop()


    '''
        Method : _init_bs
        Description : Get html document from url
    '''
    def _init_bs(self, url):
        try:
            html = urlopen(url).read().decode('cp949')
            bs = BeautifulSoup(html, 'html.parser')
            return bs
        except Exception as e:
            print(type(e), e)
    


    '''
        Method : _init_cur_page
        Description : init cur page by bs4
    '''
    def _init_cur_page(self):
        self.bs = self._init_bs(self.url)


    '''
        Method : _next
        Description : Return whether the next page exists
    '''
    def _next(self):
        return False


    '''
        Method : _get_list
        Description : Get news list from current page
    '''
    def _get_list(self):
        return []


    # '''
    #     Method : _loop
    #     Description : Run crawling
    # '''
    # def _loop(self):
    #     while True:
    #         self._sleep(sec=4)
    #         self.bs = self._init_bs(self.url)
    #
    #         for page in self._get_list():
    #             self.heads.append(self._get_head(page))
    #             self.bodys.append(self._get_body(page))
    #
    #         if not self._next() or True:
    #             break


    '''
        Method : _sleep
        Description : Giving a crawling delay
    '''
    def _sleep(self, sec):
        sleep(random() * sec)


    '''
        Method : _get_head
        Description : return news title
    '''
    def _get_head(self, page):
        self.bs = self._init_bs(self.url)
        w = bs.find('p').get_text()

        return w


    '''
        Method : _get_body
        Description : return news content
    '''
    def _get_body(self, page):
        return 'temp'
