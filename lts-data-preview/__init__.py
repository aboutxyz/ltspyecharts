# -*- coding:utf-8 -*-
import sys
import requests,json
from requests import get
from flask import Flask, render_template,request,session
import MySQLdb

app = Flask(__name__)
app.secret_key = 'forget it you can never guess'
error_msg = u'请输入船名航次'

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')
	
@app.route('/require/', methods=["GET","POST"])
def revoyage():
    if request.method != "POST":
        return render_template('voyage.html',data = error_msg)
    else:
        vesselname = request.form['vesselname']
        data={'vesselname':vesselname}
        r = requests.get('http://127.0.0.1:7777/vessel',params = data)
        data = json.loads(r.text)
        return render_template('voyage.html',vesselname=vesselname,data=data)

if __name__ == '__main__':
    app.run()
		



