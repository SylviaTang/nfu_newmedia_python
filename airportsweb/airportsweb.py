 # -*- coding: utf-8 -*- 
import calcudistance  
import json
with open('data\gaycone.json', 'r', encoding='utf8') as infile:
           dd = json.load (infile)
a = calcudistance.airport_list_name()
a_list = [k for k in dd.keys()]

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_list_items = a_list ,
                           the_title='欢迎使用查询国内两个机场之间里程之工具！')

@app.route('/pickairport', methods=['POST'])
def searchairports() -> 'html':
    airportone = request.form['user_airportone']
    airporttwo = request.form['user_airporttwo']
    return render_template('results.html',
                           the_title = '以下是您选取的机场：',
                           the_airportone = airportone,
                           the_airporttwo = airporttwo
                           )

if __name__ == '__main__':
    app.run(debug=True)

