'''
    description : crawler main function
'''
'''
    import list
'''
from crawler.Inews_Crawler import Inews_Crawler
from datetime import datetime
import re
import random
import os



def loop(crawler,directory):
    try :
        for k in range(220):
            page = crawler._get_next_month()
            crawler._sleep(sec=random.random() + 3.0)
            crawler._init_cur_page()
            for k in crawler._next_paging(page):
                if len(crawler._get_list(k)) == 0 :
                    break
                else:
                    for j in crawler._get_list(k):
                        headline = crawler._get_head(j)
                        merge = directory +'/line/'+ headline + '.txt'
                        original =directory + '/original/'+headline + '.txt'
                        remove_tag = directory + '/remove_tag/'+headline + '.txt'
                        merge_file = open(merge,'a+t')
                        original_file = open(original,'a+t')
                        remove_tag_file = open(remove_tag, 'a+t')
                        original_file.write(page + "\n")
                        original_file.write(crawler._get_original(j)+"\n")
                        remove_tag_file.write(headline+"\n")
                        remove_tag_file.write(crawler._remove_tag(j)+"\n")                    
                        merge_file.write(headline+"\n")
                        for x in crawler._get_body(j):
                            merge_file.write(x+"\n")
                        original_file.close()
                        remove_tag_file.close()
                        merge_file.close()
    except Exception as e:
        print(e)
        crawler._sleep(sec=random.random()+3.0)
        loop(crawler, directory)
    return heads,bodys

    

# \[[/s/S]*\]

'''
    main function
'''
if __name__ == '__main__':
    url = "http://news.inews24.com/php/news_list.php?g_menu=020100&date=199912&page=1"
    base_url = 'http://news.inews24.com'
    crawler = Inews_Crawler(url = url, base_url = base_url)
    url_list = crawler._get_url_list()
    category_list = crawler._get_category_list()
    for i in range(len(url_list)):
        url = base_url + url_list[i] + "&date=199912&page=1"
        crawler = Inews_Crawler(url = url, base_url = base_url)
        cwd = os.getcwd()
        directory = cwd+'/'+category_list[i]
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.mkdir(directory + '/line/')
        os.mkdir(directory + '/original/')
        os.mkdir(directory + '/remove_tag/')
        heads, bodys = loop(crawler,directory)

    # something to do ...
