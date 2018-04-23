'''
    Title : km_politic_Crawler.pyㄴ
'''

'''
    import list
'''
from crawler.BaseCrawler import BaseCrawler
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
import datetime
'''
    class : Ja_crawler
'''
class spo_crawler(BaseCrawler):
    def __init__(self, url, base_url=None):
        self.base_url = base_url if base_url else url
        super().__init__(url)


    def _get_list(self):
        html = urlopen(self.url).read().decode('euc-kr')
        bs = BeautifulSoup(html, 'html.parser')
        base_url = self.base_url
        ret_list = [base_url + tit.find('a').get('href') for tit in bs.find_all('li', {'class': 'left'})]
        return ret_list

    def _get_body(self, page):
        bs = self._init_bs(page)
        body = bs.find('div',{'id':'GS_Content'}).text
        txt = body
        txt = re.sub("<!--[\s\S]*-->", "", txt, re.DOTALL)
        i = txt
        i = re.sub('&nbsp;', ' ', i)
        i = re.sub('    ','',i)
        i = re.sub("\t","",i)
        i = re.sub("\n","",i)
        i = re.sub("\r","",i)
        i = re.sub("\. ",".",i)
        i = re.sub("\xa0","",i)
        i = re.sub("&apos;","",i)
        # i = re.sub('\([a-zA-Z0-9]*.*\)',"",i)
        i = re.sub(".*기자","",i)
        i = re.sub("사진",'',i)
        i = re.sub("출처",'',i)
        i = re.sub('\[.*\]','',i)
        i = re.sub(']','',i)
        i = re.sub('=','',i)
        i = re.sub('([\.0-9a-z_-]+)@([0-9a-z_-]+)(\.[0-9a-z_-]+){1,2}','',i)
        i = re.sub('관련 기사.*','',i)
        return i
    def _get_next_page(self):
        url = self.url
        cur_page = int(re.findall('\d+',url)[0])
        next_page = cur_page + 1
        self.url = url.replace(str(cur_page),str(next_page),1)
        print(self.url)

        
