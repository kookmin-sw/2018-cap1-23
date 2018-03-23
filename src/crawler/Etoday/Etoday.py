from crawler.E_crawler import E_crawler

from datetime import datetime
import re
import random
import os

category1= ['http://www.etoday.co.kr/news/section/subsection.php?MID=2100&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=2200&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1600&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1100&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1200&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1800&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1300&page=2',
       'http://www.etoday.co.kr/news/section/subsection.php?MID=1400&page=2']
category2 = ['증권_금융','기업','여성','정치','경제','사회','국제','부동산']

base_url = 'http://www.etoday.co.kr'

# def next_file(file_name):
#     from_change = int(re.findall('\d+', file_name)[0])
#     to_change = from_change+1
#     new_name = file_name.replace(str(from_change), str(to_change))
#     return new_name
# def today_date():
#     year = datetime.today().year
    
#     month = datetime.today().month
#     if month < 10:
#         month = '0' + str(month)
#     date = datetime.today().day
#     if date < 10:
#         date = '0' + str(date)
#     today_date = str(year)+'-'+str(month)+'-'+str(date)
    
#     return today_date

def loop(crawler,directory):
    heads = []
    bodys = []

    while True:
        crawler._sleep(sec=random.random() + 3.0)
        crawler._init_cur_page()
        
        for k in crawler._next_paging():
            for page in crawler._get_list(k):
                headline = crawler._get_headline(page)
                merge = directory +'/line/'+ headline + '.txt'
                original =directory + '/original/'+headline + '.txt'
                remove_tag = directory + '/remove_tag/'+headline + '.txt'
                merge_file = open(merge,'a+t')
                original_file = open(original,'a+t')
                remove_tag_file = open(remove_tag, 'a+t')
                original_file.write(page + "\n")
                original_file.write(crawler._get_original(page)+"\n")
                remove_tag_file.write(headline+"\n")
                remove_tag_file.write(crawler._remove_tag(page)+"\n")                    
                merge_file.write(headline+"\n")
                for x in crawler._get_body(page):
                    merge_file.write(x+"\n")
                original_file.close()
                remove_tag_file.close()
                merge_file.close()

        # except Exception as e:
        #     print("error")
        #     print(e)
        #     crawler._sleep(sec=random.random() + 2.0)
        #     loop(crawler,directory)
        if not crawler._next():
            break

'''
    main function
'''
if __name__ == '__main__':
    for i in range(len(category1)):
        now_category = category2[i]
        cwd = os.getcwd()
        directory = cwd+'/'+now_category
        if not os.path.exists(directory):
            os.mkdir(directory)
            os.mkdir(directory + '/line/')
            os.mkdir(directory + '/original/')
            os.mkdir(directory + '/remove_tag/')
        url = category1[i]
        crawler = E_crawler(url=url, base_url=base_url)

        loop(crawler,directory)

