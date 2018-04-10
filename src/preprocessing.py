from konlpy.tag import Twitter
from pprint import pprint
import io
import nltk

pos_tagger = Twitter()

def tokenize(doc): #형태소분석
	return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

train_txt = open('train_1.txt', mode='r',encoding='utf-8').read()
data = tokenize(train_txt)

tokens = [d for d in data]
text = nltk.Text(tokens, name='NMSC')
print(text)
print(len(text.tokens))                 # returns number of tokens
# => 2194536
print(len(set(text.tokens)))            # returns number of unique tokens
# => 48765
pprint(text.vocab().most_common(100)) 
text.plot(20)