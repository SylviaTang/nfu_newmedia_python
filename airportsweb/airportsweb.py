 # -*- coding: utf-8 -*- 
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎来到网上查询国内两个机场之间的里程！')

@app.route('/pickairport', methods=['POST'])
def searchairports() -> 'html':
    airportone = request.form['airportone']
    airporttwo = request.form['airporttwo']
    return render_template('results.html',
                           the_title = '以下是您选取的机场：',
                           the_airportone = airportone,
                           the_airporttwo = airporttwo
                           )

if __name__ == '__main__':
    app.run(debug=True)

import json
with open('gaycone.json', 'r',encoding = 'utf8') as infile:
    dddddd = json.load (infile)
    dddddd.keys()
    airportone = dddddd['']
    airporttwo = dddddd['']

def distance(a1,a2):
    print(a1,a2)
    d = a1['longitude']-a2['longitude']
    return(d)
    
distance(airportone,airporttwo)
