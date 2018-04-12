#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request, render_template
import json
from flask_jsonpify import jsonify
#from flask_oauthlib.provider import OAuth2Provider
import gensim
import sys
import imp
imp.reload(sys)

app = Flask(__name__)

@app.route('/success/<text>')
def success_doc2vec(text):
       model = gensim.models.Doc2Vec.load("/home/nlpserver/Desktop/Lee/model/doc2vec.model")
      # print(type(text.encode('utf8')))
       result = model.most_similar(text,topn=20)
      # return json.dumps(result,ensure_ascii=False,encoding='utf-8') 
      # print("=====================",result)
       return json.dumps(result, ensure_ascii=False) 

@app.route('/doc2vec', methods = ['POST','GET'])
def get_text():
       if request.method == 'POST':
             user1 = request.form['get_text']
             return redirect(url_for('success_doc2vec' , text = user1))
       else :
             user1 = request.args.get('get_text')
             return redirect(url_for('success_doc2vec',text = user1))

@app.route('/')
def index():
       return "hello world"
       
if __name__ == '__main__' :
       app.run(host='0.0.0.0',debug=True) 