'''
    description : crawler main function
'''
'''
    import list
'''
from crawler.TennisCrawler import TennisCrawler
import re
import random
import os



def next_file(file_name):
    from_change = int(re.findall('\d+', file_name)[0])
    to_change = from_change+1
    new_name = file_name.replace(str(from_change), str(to_change))
    return new_name


def loop(crawler, directory):
    while True:
        crawler._sleep(sec=random.random() + 2.0)
        crawler._init_cur_page()
        
        try:
            for page in crawler._get_list():
                headline = crawler._get_head(page)
                merge = directory + '/line/'+headline+'/merge.txt'
                original = directory + '/original/'+headline+'/original_html.txt'
                remove_tag = directory + '/remove_tag/'+headline+'/remove_tag.txt'
                
                merge_file = open(merge,'a+t')
                original_file = open(original,'a+t')
                remove_tag_file = open(remove_tag, 'a+t')
                original_file.write(page + "\n")
                original_file.write(crawler._get_original(page)+"\n")
                    #print("d")
                remove_tag_file.write(crawler._get_head(page)+"\n")
                remove_tag_file.write(crawler._remove_tag(page)+"\n")
                merge_file.write(crawler._get_head(page))
                merge_file.write("\n")
                for x in crawler._get_body(page):
                    merge_file.write(x+"\n")

            if not crawler._next():
                break
        except Exception as e:
            print(e)
            crawler._make_next()

def club_loop(crawler,directory):
    while True:
        crawler._sleep(sec=random.random() + 2.0)
        crawler._init_cur_page()
        
        try :
            for page in crawler._get_list():
                headline = crawler._c_get_headline(page)
                merge = directory + '/line/'+headline+'/merge.txt'
                original = directory + '/original/'+headline+'/original_html.txt'
                remove_tag = directory + '/remove_tag/'+headline+'/remove_tag.txt'
                merge_file = open(merge,'a+t')
                original_file = open(original,'a+t')
                remove_tag_file = open(remove_tag, 'a+t')
                original_file.write(page + "\n")
                original_file.write(crawler._get_original(page)+"\n")
                    #print("d")
                remove_tag_file.write(crawler._c_get_head(page)+"\n")
                remove_tag_file.write(crawler._remove_tag(page)+"\n")
                merge_file.write(crawler._c_get_head(page))
                merge_file.write("\n")
                for x in crawler._get_body(page):
                    merge_file.write(x+"\n")

            if not crawler._next():
                break
        except Exception as e:
            print(e)
            crawler._make_next()

# \[[/s/S]*\]

'''
    main function
'''
if __name__ == '__main__':
    now_category = 'news'
    cwd = os.getcwd()
    directory = cwd+'/'+now_category
    if not os.path.exists(directory):
        os.mkdir(directory)
        os.mkdir(directory + '/line/')
        os.mkdir(directory + '/original/')
        os.mkdir(directory + '/remove_tag/')

    url = 'http://www.tennis.co.kr/News/List?category=internal&page=1'
    base_url = 'http://tennis.co.kr'
    crawler = TennisCrawler(url=url, base_url=base_url)
    loop(crawler, directory)

    now_category = 'club'
    cwd = os.getcwd()
    directory = cwd+'/'+now_category
    if not os.path.exists(directory):
        os.mkdir(directory)
        os.mkdir(directory + '/line/')
        os.mkdir(directory + '/original/')
        os.mkdir(directory + '/remove_tag/')
    url = 'http://tennis.co.kr/mCafe/PromotionList?category=promotion&page=1'
    base_url = 'http://tennis.co.kr'
    crawler = TennisCrawler(url = url, base_url = base_url)
    club_loop(crawler, directory2)

    # something to do ...
