# API app for controlling AV devices

from flask import Flask
import json
import directv

dtv = DirecTV("192.168.88.253")
app = Flask(__name__)

@app.route('/')
def index():
	i={
		'name':'Petraberg AV System',
		'location':'Minneapolis, MN'
	}
    return json.dumps(i)

@app.route('/dtv/key/<key>')
def dtv_key(key):
	dtv.sendkey(key,'keyPress')

@app.route('/dtv/chan/<chan>')
def dtv_key(chan):
	dtv.sendchan(chan,0)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
