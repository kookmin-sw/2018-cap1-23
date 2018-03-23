'''
    description : crawler main function
'''
'''
    import list
'''
from crawler.Km_Crawler import Km_Crawler
from datetime import datetime
import re
import random
import os

#'pol', 'eco', 'soc', 'reg','int', 'cul', 'lif', 'hea', 'tra', 'per',
#'policy','economy', 'society','region','international','culture','life','health','travel','human',
category = ['ent']
file_category = ['entertainment']


def next_file(file_name):
    from_change = int(re.findall('\d+', file_name)[0])
    to_change = from_change+1
    new_name = file_name.replace(str(from_change), str(to_change))
    return new_name
def today_date():
    today = datetime.today()
    today = today.strftime("%Y%m%d")
    
    return today

def loop(crawler,directory):
    heads = []
    bodys = []
    original = directory

    while crawler._last_date() > 20090101:
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
            crawler._next()
            loop(crawler,directory)
        print(crawler._next())
        

    return heads, bodys

# \[[/s/S]*\]

'''
    main function
'''
if __name__ == '__main__':
    for i in range(0,len(category)):
        url = 'http://news.kmib.co.kr/article/list_all.asp?sid1='+category[i]+'&sid2=&sdate='+today_date()
        base_url = 'http://news.kmib.co.kr/article/list_all.asp?sid1='+category[i]+'&sid2=&sdate='
        crawler = Km_Crawler(url=url, base_url=base_url)
        cwd = os.getcwd()
        directory = cwd+'/'+category[i]
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.mkdir(directory + '/line/')
        os.mkdir(directory + '/original/')
        os.mkdir(directory + '/remove_tag/')
        heads, bodys = loop(crawler,directory)

    # something to do ...
