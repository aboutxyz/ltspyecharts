# -*- coding:utf-8 -*-
import sys
import requests,json
from requests import get
from flask import Flask, render_template,request,session
import MySQLdb
from config import *

app = Flask(__name__)
app.secret_key = 'forget it you can never guess'
error_msg = u'请输入船名航次'


# def surround_by_quote(vai):
    # return '"%s"' % vai
# env=app.jinja_env
# env.filters["surround_by_quotes"] = surround_by_quote   #前面为html 中用的，后面是函数名

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')
	
@app.route('/statics/<vname>', methods=["GET","POST"])
def revoyage(vname):
    if vname=="month-voyage":
        return render_template("statics/month-voyage.html",voyagevaluedict=voyagevaluedict)

if __name__ == '__main__':
    app.run(debug=True)
		



