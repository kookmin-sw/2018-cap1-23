import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('text.txt').read()
wordcloud = WordCloud().generate(text)
wordcloud.words_
plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
fig = plt.gcf()
#plt.show()
fig.savefig('GG1.png')
