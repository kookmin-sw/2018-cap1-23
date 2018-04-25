"""
    title : main_xsports.py
    author : lgy
"""

"""
    import
"""
import sys #for arg in main
from crawler.Xsports import Xsports
import re
import os
import datetime
import time

"""
    variable
"""
url = {'http://www.xportsnews.com/?ac=article_list&cate_indexno=178&page=1': 'jenter',
       'http://www.xportsnews.com/?ac=article_list&cate_indexno=42&page=1': 'jsports'}

base_url = 'http://www.xportsnews.com/'

OUT_PATH = "out_file/"

TXT = ".txt"

"""
    functions
"""

######################################

def loop(crawler, key):
    out = open(OUT_PATH+"xsports.txt", 'a')
   
    while True:
        crawler._sleep(sec = 4)
        crawler._init_cur_page()

        for page in crawler._get_list():
            
            print(page)

            bodys= crawler._get_body(page)

            # print(bodys)

            # for j in bodys :
            #     out.write(j)

            for j in bodys:
                out.write(j)
            out.write("\r\n")

        if not crawler._next():
            break

    out.close()
        

######################################

def main():

     for i in url.keys() :
        print(url[i])
        crawler = Xsports(url=i, next='&page=1', decode='utf8', base_url=base_url, category_url=url[i])
        loop(crawler,i)

if __name__ == "__main__":
    main()
