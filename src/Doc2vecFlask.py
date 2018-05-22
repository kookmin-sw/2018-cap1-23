#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask.ext.cache import Cache
from flask import Flask, redirect, url_for, request, render_template,send_file
import json
from flask_jsonpify import jsonify
import gensim
import sys
import imp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
imp.reload(sys)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']= 0
app.config["CACHE_TYPE"] = "null"

@app.route('/success/<text>')
def success_doc2vec(text):
      cache = Cache()
      model = gensim.models.Doc2Vec.load("/Users/seungeonlee/Desktop/capstone/2018-cap1-23/src/model/doc2vec.model")
      result = model.most_similar(text.strip(),topn=10)
      result2 = model.most_similar(text.strip(),topn=20)
      output = []
      for i in range(len(result)):
            output.append(result[i][0])
      text = ""
      for i in range(len(output)):
            text += output[i] + " "
      word = open('word.txt','w')

      for i in result2:
            word.write('\"'+i[0]+'\":'+str(i[1])+"\n")
      word.close()
      mylist = open('word.txt').read()
      
      wordcloud = WordCloud(background_color='white',font_path ="/NEXON Football Gothic B.otf").generate(mylist)
      wordcloud.words_
      plt.figure(figsize=(5,5))
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis("off")
      fig = plt.gcf()

      image_num = random.randrange(1,100)
      image_name = "/static/image/"+str(image_num)+".png"
      print(image_name)
      fig.savefig('/Users/seungeonlee/Desktop/capstone/2018-cap1-23/src/static/image/GG.png') 

      return redirect(url_for("_html", result=text))


@app.route('/doc2vec', methods = ['POST','GET'])
def get_text():
       if request.method == 'POST':
             user1 = request.form['get_text']
             return redirect(url_for('success_doc2vec' , text = user1))
       else :
             user1 = request.args.get('get_text')
             return redirect(url_for('success_doc2vec',text = user1))



@app.route('/')
@app.route('/html')
@app.route('/<result>')
def _html(result = ""):
	return render_template('Doc2vec.html',result=result)
@app.after_request
def add_header(response):
      response.headers['Cache-Control'] = 'no-store, no-cache, must-reavlidate, post-check=0, pre-check=0, max-age=0'
      response.headers['Pragma'] = 'no-cache'
      response.headers['Expires'] = '-1'
      return response

       
if __name__ == '__main__' :
       app.run(host='0.0.0.0',debug=True)
