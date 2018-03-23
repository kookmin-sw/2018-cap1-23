import os, glob
import re


def classify_line(directory,filename):
	count = 0
	file1_n = directory + '/sentence.txt'
	file2_n = directory + '/nonsentence.txt'
	#file3_n = directory + '/check_quote.txt'
	file4_n = directory + '/slice_quote.txt'

	file1 = open(file1_n,'a+t')
	file2 = open(file2_n,'a+t')
	#file3 = open(file3_n, 'a+t')
	file4 = open(file4_n, 'w+t')
	pattern1 = re.compile("[^가-힣a-zA-Z\s\.\,0-9\'\"\·\%\-\!\?]")
	pattern2 = re.compile('[가-힣[.]]')
	# pattern3 = re.compile('“')
	# pattern3_1 = re.compile('"')
	# pattern3_2 = re.compile('\.”')
	pattern4 = re.compile('^\s')
	pattern5 = re.compile('^[a-zA-Z0-9가-힣]')
	pattern6 = re.compile('[.]$')
	pattern3 = re.compile('\"')


	original = open(filename)
	
	p = original.read()

	for i in range(len(p)):
		if(p[i] =='\"'):
			count += 1
			file4.write(p[i])
		elif(p[i] == "\n"):
			if count%2 == 0 :
				file4.write(p[i])
				i+=1
		else:
			file4.write(p[i])
	file4.close()
	original = open(file4_n,'r+t')

	lines = original.readlines()


	for line in range(1,len(lines)):
		line = lines[line]
		# count = 0
		line = re.sub('\([a-zA-Z0-9]*.*\)',"",line)
		line = re.sub('뉴시스','',line)
		line = re.sub('.*국민일보.*','',line)
		line = re.sub('\[.*\]','',line)
		line = re.sub('\{.*\}','',line)
		line = re.sub('^\n','',line)
		line = re.sub("^[ ]",'',line)
		line = re.sub("사진.*",'',line)
		line = re.sub(".*=.*",'',line)
		line = re.sub("“",'"',line)
		line = re.sub('”','"',line)
		line = re.sub(".*기자","",line)
		line = re.sub("  "," ",line)
		line = re.sub("‘","'", line)
		line = re.sub("’","'",line)


		result6 = re.search(pattern6, line)
		result5 = re.search(pattern5, line)
		result1 = re.findall(pattern1, line)
		result3 = re.findall(pattern3, line)

		if len(line.split(" "))<5: #less than 5 words
			file2.write(line)
			continue
		elif result6 is None:  # not ending with dot
			file2.write(line)
			continue
		elif result5 is None:  # not start with word
			file2.write(line)
			continue
		elif len(result1)>0: #remove special char
			file2.write(line)
			continue
		elif len(result3)>0:
			file1.write(line)
			continue
		else :
			file1.write(line)
if __name__ == '__main__':
    cwd = os.getcwd()
    directory = cwd+'/'+ 'classify'
    if not os.path.exists(directory):
    	os.mkdir(directory)
    filelist = glob.glob("*.txt")
    for i in filelist :
    	if os.path.isfile(i):
    		classify_line(directory, i)




#[^가-힝0-9a-zA-Z\\s]
