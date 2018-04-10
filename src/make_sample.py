import os, glob
import re


def sample_line(directory,filename):
	file_n = directory + '/sample.txt'
	file = open(file_n,'a+t')
	original = open(filename)
	
	p = original.readlines()
	# file.write("\n")
	# file.write("****************************")
	# file.write("!!!!!")
	for i in range(1,len(p)):
		line = p[i]
		line = re.sub('\([a-zA-Z0-9]*.*\)',"",line)
		line = re.sub('뉴시스','',line)
		line = re.sub('.*국민일보.*','',line)
		line = re.sub('\[.*\]','',line)
		line = re.sub('\{.*\}','',line)
		line = re.sub("^[ ]",'',line)
		line = re.sub("사진.*",'',line)
		line = re.sub(".*=.*",'',line)
		line = re.sub("“",'"',line)
		line = re.sub('”','"',line)
		line = re.sub(".*기자","",line)
		line = re.sub("  "," ",line)
		line = re.sub("‘","'", line)
		line = re.sub("’","'",line)
		line = re.sub("\n", "", line)
		if( i == len(p)-1):
			file.write(line+"\n")
		else:
			file.write(line)
	#file.write("\n")

if __name__ == '__main__':
    cwd = os.getcwd()
    directory = cwd+'/'+ 'sample'
    if not os.path.exists(directory):
    	os.mkdir(directory)
    filelist = glob.glob("*.txt")
    for i in filelist :
    	if os.path.isfile(i):
    		sample_line(directory, i)




#[^가-힝0-9a-zA-Z\\s]
