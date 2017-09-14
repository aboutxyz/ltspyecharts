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
	
@app.route('/statics/<vname>', methods=["GET","POST"])
def revoyage(vname):
    if vname=="m-v":
        return render_template("statics/m-v.html")

if __name__ == '__main__':
    app.run(debug=True)
		



