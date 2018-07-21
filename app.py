from flask import Flask, render_template,request
from jinja2 import Template 
import twint
import io
import time
import os
import pandas as pd

#postgresql-convex-23455

app = Flask(__name__)

@app.route('/twittersearch')
def twittersearchpage():
    return render_template('twittersearch.html')

@app.route('/searchresults',methods=['POST','GET'])
def searchResults():
    c = twint.Config()
    c.Username = request.form['username']
    c.Store_csv = True
    c.Custom = ["username", "tweet"] 
    c.Limit = 20
    c.Output = "static/twitter.csv"
    twint.run.Search(c)
    df = pd.read_csv('static/twitter.csv')
    df.to_html("templates/blah.html")
    
    # with open("static/twitter.csv") as f:
    #     s = f.read() 
    # lst = []
    # buf = io.StringIO(s)
    # for line in buf.read():
    #     lst.append(line)
    # print(lst)
    # filename = 'twitter.csv'
    # f = open(filename, "w+")
    # f.truncate()
    # f.close()
    return render_template("blah.html")


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)