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

'''
    class : km_politic_Crawler
'''
class Km_Crawler(BaseCrawler):
    def __init__(self, url, base_url=None):
        self.base_url = base_url if base_url else url
        super().__init__(url)


    def _next(self):
        url = self.url
        html = urlopen(url).read().decode('cp949')
        bs = BeautifulSoup(html, 'html.parser')
        date_list = bs.find_all('li')
        on_list = bs.find('li',{'class':'on'})
        on_date = on_list.find('a').get('href')
        new_date_list = []
        for i in range(len(date_list)):
            new_date_list.append(date_list[i].find('a').get('href'))
        idx = new_date_list.index(on_date) + 1
        from_change = int(re.findall('\d+', new_date_list[idx])[2])
        self.url = self.base_url+ str(from_change)
        return self.url

    def _last_date(self):
        url = self.url
        date = int(re.findall('\d+', url)[2])
        return date


    def _next_paging(self):
        url = self.url
        html = urlopen(url).read().decode('cp949')
        bs = BeautifulSoup(html, 'html.parser')
        try:
            ref = bs.find('a',{'class':'end'}).get('href')
            end_page_num = int(re.findall('\d+', ref)[2])
            page_link=[]
            for x in range(1,end_page_num+1):
                page_link.append(self.url+'&page='+str(x))
            return page_link
        except Exception as e:
            page_link = []
        return page_link

    def _get_list(self,page):
        mylist = []
        url = page
        html = urlopen(url).read().decode('cp949')
        bs = BeautifulSoup(html, 'html.parser')
        ref = bs.find_all('dl',{"class":"nws"})
        if len(ref) == 0 :
            return mylist
        else :
            for i in range(len(ref)):
                mylist.append('http://news.kmib.co.kr/article/'+ref[i].find('a').get('href'))
            return mylist

    def _get_head(self, page):
        bs = self._init_bs(page)
        head = bs.find('div',{'class':'nwsti'})
        head = head.text.split("\n")
       # head[1] = re.sub('\[.*\]','',head[1])
        return head[1]

    def _get_original(self, page): #태그제거하지않은 본문 내용
        html = urlopen(page)
        txt = html.read().decode("cp949")
        return txt
    
    def _remove_tag(self,page): #태그제거한 본문내용
        html = urlopen(page)
        txt = html.read().decode("cp949")
        bs = self._init_bs(page)
        body = bs.find('div',{'class':'tx'})
        txt = body.text
        return txt

    def _get_body(self, page):
        bs = self._init_bs(page)
        body = bs.find('div', {'class': 'tx'})
        txt = body.text
        txt = re.sub("<!--[\s\S]*-->", "", txt, re.DOTALL)
        i = txt
        i = re.sub('    ','',i)
        i = re.sub("\t","",i)
        i = re.sub("\n","",i)
        i = re.sub("\r","",i)
        i = re.sub("\. ",".",i)
        i = re.sub("&apos;","",i)
        line_lst = i.split("다.")
        temp_txt = []
        for j in range(len(line_lst)-1):
            temp_txt.append(line_lst[j].strip()+"다.")
        return temp_txt


        date_list = bs.find_all('li')
        
