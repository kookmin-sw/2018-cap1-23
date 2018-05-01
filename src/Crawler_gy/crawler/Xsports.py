'''
    Title : Xsports.py
    Author : lgy
'''

'''
    import list
'''

'''
    class : Xsports
'''
from crawler.BaseCrawler import BaseCrawler
import re
import datetime
from datetime import time

class Xsports(BaseCrawler):
    def __init__(self, url, next, decode, category_url, base_url=None):
        self.base_url = base_url if base_url else url
        self.next_url = next
        self.decode = decode
        self.category_url = category_url
        # self.category = category
        super().__init__(url)


    def _next(self):
        try:
            if (len(self.bs.find('a', {'class': 'next'}))==0) :
                return False
            from_change = int(re.findall('\d+',self.next_url)[0])
            to_change = from_change+1
            next_url = self.next_url.replace(str(from_change),str(to_change))
            new_url = self.url.replace(str(self.next_url), str(next_url))
            print("next",next_url)
            self.next_url = next_url
            self.url = new_url
            return True
        
        except:
            from_change = int(re.findall('\d+',self.next_url)[0])
            to_change = from_change+2
            next_url = self.next_url.replace(str(from_change),str(to_change))
            new_url = self.url.replace(str(self.next_url), str(next_url))
            print("next",next_url)
            self.next_url = next_url
            self.url = new_url
            return True


    def _get_list(self):
        item_list = self.bs.find_all('div', {'class': 'thumb'})

        ret_list = [self.base_url  + self.category_url+
        i_list.find_all('a')[0].get('href') for i_list in item_list]

        """
        print("---------")
        [print(i) for i in ret_list]
        print("========")
"""
        return ret_list

    def delEnter(self, txt):
        """
        """
        t = re.sub('\r\n','',txt)
        t = re.sub('\n','',t)
        t = re.sub('\t','',t)
        t = re.sub('([\.0-9a-z_-]+)@([0-9a-z_-]+)(\.[0-9a-z_-]+){1,2}','',t)
        t = re.sub('\/','',t)
        t = re.sub('사진 = .*','',t)
        t = re.sub('사진=.*','',t)
        t = re.sub('\[.*기자\]','',t)




        return t

    def re_enter(txt):
        text = re.sub("다\.", "다.\n", txt)

        return text

    def _get_head(self, page):
        try :
            bs = self._init_bs(page)
            head = bs.find_all("title")
            return head[0].text
        except : 
            return ""

    def _get_body(self, page):
        try :
            bs = self._init_bs(page)
            body = bs.find_all(id='CmAdContent')[0].text.split(';')[3]
            # print(body)
            delE_body = self.delEnter(body)
            print(delE_body)
            return delE_body
        except :
            return ""

    # def _get_date(self,page):
    #     bs = self._init_bs(page)
    #     t1 = bs.find('div',{'class':'byline'})
    #     t2 = t1.find('em').text
    #     date =re.findall('\d+', t2)
    #     year = int(date[0])
    #     month =int(date[1])
    #     day = int(date[2])

    #     return datetime.date(year,month,day)


    # def _get_time(self,page):
    #     bs = self._init_bs(page)
    #     t1 = bs.find('div', {'class': 'byline'})
    #     t2 = t1.find('em').text
    #     t = re.findall('\d+', t2)
    #     hour = int(t[3])
    #     minute = int(t[4])

    #     return datetime.time(hour,minute)


    def _get_datetime(self, page):
        bs = self._init_bs(page)
        t1 = bs.find('div',{'class':'byline'})
        t2 = t1.find('em').text
        date =re.findall('\d+', t2)
        year = int(date[0])
        month =int(date[1])
        day = int(date[2])
        hour = int(date[3])
        minute = int(date[4])

        return datetime.date(year,month,day), datetime.time(hour,minute)

    def _init_c(self,page) :
        self.url = page
        self.heads = []
        self.bodys = []
        self.next_url = '&page=1'
        self.file_name = 1