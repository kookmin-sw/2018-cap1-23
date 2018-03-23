'''
    Title : TennisCrawler.py
    Author : ngh
'''

'''
    import list
'''
from crawler.BaseCrawler import BaseCrawler
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''
    class : TennisCrawler
'''
class TennisCrawler(BaseCrawler):
    def __init__(self, url, base_url=None):
        self.base_url = base_url if base_url else url
        super().__init__(url)


    def _next(self):
        next_lst = self.bs.find_all('a', {'class' : 'num_next'})

        if len(next_lst) == 2:
            next_btn = next_lst[0]
            self.url = self.base_url + next_btn.get('href')
            return True

        else:
            return False
    def _make_next(self):
        new_url = self.url
        from_change = int(re.findall('\d+', self.url)[0])
        to_change = from_change+1
        new_url = self.url.replace(str(from_change), str(to_change))
        self.url = new_url
        return True


    def _get_list(self):


        ret_list = [self.base_url + tit.find('a').get('href')
                for tit in self.bs.find_all('dt', {'class' : 'tit'})]

        return ret_list

    def _get_head(self, page):
        bs = self._init_bs(page)
        head = bs.find('dt', {'class' : 'tit'}).text


        return head

    def _get_original(self, page): #태그제거하지않은 본문 내용
        html = urlopen(page)
        txt = html.read().decode("utf8")
        return txt
    
    def _remove_tag(self,page): #태그제거한 본문내용
        html = urlopen(page)
        txt = html.read().decode("utf8")
        bs = self._init_bs(page)
        body = bs.find('div',{'class':'newstxt'})
        txt = body.text
        return txt

    def _c_get_head(self, page):
        bs = self._init_bs(page)
        head = bs.find('div', {'class' : 'tit'})
        head = head.text
        head = re.sub("\t", "", head)
        head = re.sub("\n", "", head)
        head = re.sub("\r", "", head)
        return head
    def _c_get_headline(self, page):
        bs = self._init_bs(page)
        head = bs.find('div', {'class' : 'tit'})
        head = head.text
        head = re.sub("\t", "", head)
        head = re.sub("\n", "", head)
        head = re.sub("\r", "", head)
        head = re.sub("\/","",head)
        return head
    
    def _get_headline(self,page):
        bs = self._init_bs(page)
        head = bs.find('dt', {'class' : 'tit'}).text

        head = re.sub("\/","?",head)

        return head


    def _get_body(self, page):
        # html = urlopen(page)
        # txt = html.read()
        # txt.decode("utf8")
        # bs = BeautifulSoup(txt, 'html.parser')
        # txt = bs.find('div',{'class':'newstxt'}).text
        # txt = re.sub("<!--[\s\S]*-->", "", txt, re.DOTALL)
        # i = txt
        # i = re.sub("\n ","",i)
        # i = re.sub("\t","",i)
        # i = re.sub("\n","",i)
        # i = re.sub("\r","",i)
        # i = re.sub("  ","" ,i)
        # i = re.sub('\[.*\]','',i)
        # i = re.sub('\(.*\)','',i)
        # i = re.sub('    ','',i)
        # line_lst = i.split("다.")
        # temp_txt = []
        # for j in range(len(line_lst)-1):
        #     temp_txt.append(line_lst[j].strip()+"다.")
        # return temp_txt
        html = urlopen(page)
        txt = html.read().decode("utf8")
        bs = self._init_bs(page)
        body = bs.find('div',{'class':'newstxt'})
        txt = body.text
        i = txt
        i = re.sub("\n ","",i)
        i = re.sub("\t","",i)
        i = re.sub("\n","",i)
        i = re.sub("\r","",i)
        i = re.sub("  ","" ,i)
        i = re.sub('\[.*\]','',i)
        i = re.sub('\(.*\)','',i)
        i = re.sub('    ','',i)
        line_lst = txt.split("다.")
        temp_txt = []
        for j in range(len(line_lst)-5):
            temp_txt.append(line_lst[j].strip()+"다.")
        
        
        return temp_txt


        