from crawler.Ja_crawler import Ja_crawler

from datetime import datetime
import re
import random
import os

category = ['politics','sports','money','society' ,'world','culture']
dic_category = {'politics':['assemgov', 'bluehouse' ,'diplomacy' ,'nk' ,'northkorea'],
'sports':['baseball','worldbaseball','soccer','worldsoccer','basketvolley'],
'money':['economy', 'finance' ,'stock' ,'itview'],
'society':['law', 'education' ,'accident' ,'welfare' ,'traffic' ,'environment' ,'region' ,'health'],
'world':['china', 'japan' ,'eu', 'etc'],
'culture':['book', 'perfomance','art','classic' ,'song' ,'broadcast', 'movie']}
def next_file(file_name):
    from_change = int(re.findall('\d+', file_name)[0])
    to_change = from_change+1
    new_name = file_name.replace(str(from_change), str(to_change))
    return new_name
def today_date():
    year = datetime.today().year
    
    month = datetime.today().month
    if month < 10:
        month = '0' + str(month)
    date = datetime.today().day
    if date < 10:
        date = '0' + str(date)
    today_date = str(year)+'-'+str(month)+'-'+str(date)
    
    return today_date

def loop(crawler,directory):
    heads = []
    bodys = []

    while crawler._last_date() > 20110101:
        crawler._sleep(sec=random.random() + 3.0)
        crawler._init_cur_page()
        try:
            for k in crawler._next_paging():
                for page in crawler._get_list(k):
                    headline = crawler._get_head(page)
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
        except Exception as e:
            print("error")
            print(e)
            crawler._sleep(sec=random.random() + 2.0)
            loop(crawler,directory)
        print(crawler._next())
        

    return heads, bodys


'''
    main function
'''
if __name__ == '__main__':
    for i in range(0,len(category)):
        now_category = category[i]
        cwd = os.getcwd()
        directory = cwd+'/'+now_category
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.mkdir(directory + '/line/')
        os.mkdir(directory + '/original/')
        os.mkdir(directory + '/remove_tag/')
        for j in dic_category[now_category]:
            url = 'http://news.joins.com/'+now_category+'/'+j+'/list/1?filter=All&date='+today_date()
            print(url)
            base_url = 'http://news.joins.com/'+now_category+'/'+j+'/list/1?filter=All&date='
            crawler = Ja_crawler(url=url, base_url=base_url)

            heads, bodys = loop(crawler,directory)

