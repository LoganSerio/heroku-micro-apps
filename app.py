from flask import Flask, render_template,request
import twint
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
    # if request.method == 'POST':
    filename = "static/twitter.csv"
    # # #opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.truncate()
    f.close()
    c = twint.Config()
    c.Username = request.form['username']
    c.Store_csv = True
    c.Custom = ["id", "user_id", "username", "tweet"] 
    c.Limit = 20
    c.Output = "static/twitter.csv"
    twint.run.Search(c)
    df = pd.read_csv('static/twitter.csv')
    df.to_html("templates/blah.html")
    return render_template('blah.html')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)