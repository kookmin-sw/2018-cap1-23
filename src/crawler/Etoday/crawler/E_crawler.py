'''
    Title : Etoday
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
    class : E_crawler
'''
class E_crawler(BaseCrawler):
    def __init__(self, url, base_url=None):
        self.base_url = base_url if base_url else url
        super().__init__(url)


    def _next(self):
        if (len(self.bs.find_all('a', {'class': 'next'}))==0) :
            return False

        from_change = int(re.findall('\d+',self.url)[1])
        to_change = from_change+1
        next_url = self.url.replace('page='+str(from_change),'page='+str(to_change))
        self.url = next_url
        print(self.url)
        return True


    def _get_list(self,page):
        url = page
        html = urlopen(url).read().decode('utf8')
        bs = BeautifulSoup(html, 'html.parser')
        base_url = self.base_url
        ret_list = [base_url + tit.find('a').get('href') for tit in bs.find_all('p', {'class': 'summary'})]
        return ret_list

    def _get_head(self, page):
        try :
            bs = self._init_bs(page)
            head = bs.find_all("title")
            return head[0].text
        except : 
            return ""
    def _get_headline(self,page):
        try :    
            bs = self._init_bs(page)
            head = bs.find_all("title")
            headline = head[0].text
            headline = re.sub("\/","?",headline)
            return headline
        except : 
            return ""

    
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
        body = bs.find('div', {'id': 'newsContent'}).text
        txt = body
        return txt

    def _get_body(self, page):
        bs = self._init_bs(page)
        body = bs.find('div', {'id': 'newsContent'}).text
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
        i = re.sub("google_adset\(\'Web_Sub_view_in_200x200\'\,\'A\'\)\;","",i)

        line_lst = i.split("다.")
        temp_txt = []
        for j in range(len(line_lst)-1):
            temp_txt.append(line_lst[j].strip()+"다.")
        return temp_txt
        
