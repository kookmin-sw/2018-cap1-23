#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request, render_template
import json
from flask_jsonpify import jsonify
import gensim
import sys
import imp
imp.reload(sys)

app = Flask(__name__)

@app.route('/success/<text>')
def success_doc2vec(text):
       model = gensim.models.Doc2Vec.load("/home/nlpserver/Desktop/Lee/model/doc2vec.model")

       result = model.most_similar(text.strip(),topn=10)
       output = []
       for i in range(len(result)):
           output.append(result[i][0])
       text = ""
       for i in range(len(output)):
           text += output[i] + ", "
       return redirect(url_for("_html", result=text[:-2]))

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
