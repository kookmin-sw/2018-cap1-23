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
class Ja_crawler(BaseCrawler):
    def __init__(self, url, base_url=None):
        self.base_url = base_url if base_url else url
        super().__init__(url)


    def _next(self):
        url = self.url
        print(self.url)
        cur_date = re.findall('\d+', url)[1]+re.findall('\d+', url)[2]+re.findall('\d+', url)[3]
        print(cur_date)
        cur_date = datetime.datetime.strptime(cur_date,"%Y%m%d").date()
        yesterday = cur_date - datetime.timedelta(days=1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        self.url = self.base_url + yesterday
        return self.url
    


    def _last_date(self):
        url = self.url
        cur_date = int(re.findall('\d+', url)[1]+re.findall('\d+', url)[2]+re.findall('\d+', url)[3])
        return cur_date

    def _get_list(self,page):
        url = page
        html = urlopen(url).read().decode('utf8')
        bs = BeautifulSoup(html, 'html.parser')
        base_url = "http://news.joins.com/article/"
        ret_list = [base_url + tit.find('a').get('href') for tit in bs.find_all('span', {'class': 'thumb'})]
        return ret_list

    def _get_head(self, page):
        bs = self._init_bs(page)
        head = bs.find('title').text
        return head
    
    def _next_paging(self):
        url = self.url
        html = urlopen(url).read().decode('utf8')
        bs = BeautifulSoup(html, 'html.parser')
        page_link = []
        try:
            num = bs.find_all('a',{'class':'link_page'})
            num = len(num) + 1
            page_link.append(url)
            for i in range(1, num+1):
                url = url.replace(str(i), str(i+1),1)
                page_link.append(url)
        except Exception as e:
            print(e)
        return page_link

    def _get_original(self, page): #태그제거하지않은 본문 내용
        html = urlopen(page)
        txt = html.read().decode("utf8")
        return txt
    
    def _remove_tag(self,page): #태그제거한 본문내용
        html = urlopen(page)
        txt = html.read().decode("utf8")
        bs = self._init_bs(page)
        body = bs.find('div',{'id':'article_body'}).text
        txt = body
        return txt

    def _get_body(self, page):
        bs = self._init_bs(page)
        body = bs.find('div',{'id':'article_body'}).text
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

        line_lst = i.split("다.")
        temp_txt = []
        for j in range(len(line_lst)-1):
            temp_txt.append(line_lst[j].strip()+"다.")
        return temp_txt


        date_list = bs.find_all('li')
        
