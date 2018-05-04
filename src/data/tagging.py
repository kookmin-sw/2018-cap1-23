import sys
from konlpy.tag import Twitter

def make_nouns(text):
	w_file_name = 'tagging_sample.txt'
	w_file = open(w_file_name,'a+t')
	spliter = Twitter()
	for i in range(len(text)):
		nouns = spliter.nouns(text[i])
		for j in nouns:
			w_file.write(j + " ")
		w_file.write("\n")


if __name__ == '__main__':
	r_file_name = 'sample.txt'
	r_file = open(r_file_name,'r')
	line = r_file.readlines()
	make_nouns(line)
