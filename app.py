# API app for controlling AV devices

from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
	i={
		'name':'Petraberg AV System',
		'location':'Minneapolis, MN'
	}
    return json.dumps(i)

@app.route('/tv')
def index():
	i={
		'name':'Control TV',
		'action':'Some Thing'
	}
    return json.dumps(i)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
