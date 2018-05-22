#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request, render_template,send_file
import json
from flask_jsonpify import jsonify
import gensim
import sys
import imp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
imp.reload(sys)

app = Flask(__name__)

@app.route('/success/<text>')
def success_doc2vec(text):
      model = gensim.models.Doc2Vec.load("/Users/seungeonlee/Desktop/capstone/2018-cap1-23/src/model/doc2vec.model")

      result = model.most_similar(text.strip(),topn=10)
      # wordcloud = WordCloud().generate(text)  #test 중 
      # wordcloud.words_
      # plt.figure(figsize=(5,5))
      # plt.imshow(wordcloud, interpolation='bilinear')
      # fig = plt.gcf()
      # fig.savefig('/home/nlpserver/Desktop/Lee/2018-cap1-23/src/static/image/GG.png')
      output = []
      for i in range(len(result)):
            output.append(result[i][0])
      text = ""
      for i in range(len(output)):
            text += output[i] + ", "
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
       
if __name__ == '__main__' :
       app.run(host='0.0.0.0',debug=True)
