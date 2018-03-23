'''
    Title : Inews_Crawler
'''

'''
    import list
'''
from crawler.BaseCrawler import BaseCrawler
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''
    class : Inews_Crawler
'''
class Inews_Crawler(BaseCrawler):
    def __init__(self, url, bs=None,base_url=None):
        self.base_url = base_url if base_url else url
        self.url = url
        html = urlopen(url).read().decode('cp949')
        bs = BeautifulSoup(html, 'html.parser')
        self.bs = bs
        super().__init__(url)

    def _next(self):
        date_list = self.bs.find_all('li')
        on_list = self.bs.find('li',{'class':'on'})
        on_date = on_list.find('a').get('href')
        new_date_list = []
        for i in range(len(date_list)):
            new_date_list.append(date_list[i].find('a').get('href'))
        idx = new_date_list.index(on_date) + 1
        from_change = int(re.findall('\d+', new_date_list[idx])[2])
        self.url = self.base_url+ str(from_change)
        return self.url

    def _get_list(self,page):
        url = page
        html = urlopen(url)
        txt = html.read()
        txt.decode("cp949")
        bs = BeautifulSoup(txt, 'html.parser')
        news_list = bs.find_all('a',  {'class' : 'news_list'})
        head_list = []
        for i in news_list:
            head_list.append(self.base_url + i.get('href'))
        return head_list

    def _next_paging(self,page):
        url = page
        page_link=[]
        page_num = int(re.findall('\d+', url)[3])
        page_link.append(url)
        while True:
            next_num = page_num + 1
            url = url.replace("page="+str(page_num), "page="+str(next_num))
            html = urlopen(url)
            txt = html.read()
            txt.decode("cp949")
            bs = BeautifulSoup(txt, 'html.parser')
            news_list = bs.find_all('a',  {'class' : 'news_list'})
            #print(news_list)
            #print(len(news_list))
            if len(news_list)==0 :
                return page_link
            else:
                page_link.append(url)
            page_num = next_num

        # except Exception as e:
        #     print(44)
        #     return page_link

    def _get_url_list(self):
        news_list = self.bs.find('table',  {'width' : '1001px'}).find_all('a')
        url_list = []
        list_num = len(news_list)
        for i in range(1,list_num):
            url_list.append(news_list[i].get('href'))
        return url_list

    def _get_category_list(self):
        category_list = self.bs.find('td',{'class':'w_txt'})
        category_list = category_list.text
        category_list = category_list.split("\n")
        new_list = []
        for i in range(1,16):
            new_list.append(category_list[i])       
        return new_list

    def _get_head(self, page):
        bs = self._init_bs(page)
        head = bs.find('div',{'class':'title'})
        head= head.text
        head = re.sub("   *","",head)
        
        return head
    
    def _get_next_month(self):
        url = self.url
        cur_month = int(re.findall('\d+', url)[2])
        if(cur_month%100 == 12):
            next_month = str(cur_month//100 + 1) + '01'
        else:
            next_month = str(cur_month + 1)

        url = url.replace(str(cur_month), next_month)
        self.url = url
        print(url)
        return url
    def _remove_tag(self,page):
        html = urlopen(page)
        txt = html.read().decode("cp949")
        bs = self._init_bs(page)
        body = bs.find('div', {'id': 'articleBody'}).text
        txt = body
        return txt


    def _get_original(self, page):
        html = urlopen(page)
        txt = html.read().decode("cp949")
        return txt

    def _get_body(self, page):
        bs = self._init_bs(page)
        body = bs.find('div', {'id': 'articleBody'})
        txt = body.text
        txt = re.sub("<!--[\s\S]*-->", "", txt, re.DOTALL)
        i = txt
        i = re.sub("\t","",i)
        i = re.sub("\n","",i)
        i = re.sub("\r","",i)
        i = re.sub("\. ",".",i)
        i = re.sub("&apos;","",i)
        line_lst = i.split("다.")
        temp_txt = []
        for j in range(len(line_lst)):
            if(len(line_lst[j])!=0):
                temp_txt.append(line_lst[j].strip()+"다.")
            
        return temp_txt


        
