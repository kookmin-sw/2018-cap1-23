'''
    description : crawler main function
'''
'''
    import list
'''
from crawler.spo_crawler import spo_crawler
from datetime import datetime
import re
import random
import os



def loop(crawler):
    try :
    	 # file = open('article.txt','a+t')
    	file = open('article.txt','a+t')
    	for k in range(1000):
    		crawler._sleep(sec=random.random() + 3.0)
    		crawler._init_cur_page()  
    		for j in crawler._get_list():
    			file.write(crawler._get_body(j))
    			file.write("\n")
    		crawler._get_next_page()

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
	category = ['http://sports.hankooki.com/Article/ArticleList.php?section=baseball&subsection=all&page=1',
	'http://sports.hankooki.com/Article/ArticleList.php?section=soccer&subsection=all&page=1',
	'http://sports.hankooki.com/Article/ArticleList.php?section=sports&subsection=all&page=1',
	'http://sports.hankooki.com/Article/ArticleList.php?section=entv&subsection=all&page=1']
	for i in category:
		url = i
		base_url = 'http://sports.hankooki.com'
		crawler = spo_crawler(url = url, base_url = base_url)
		heads, bodys = loop(crawler)

    # something to do ...
