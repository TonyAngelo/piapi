# API app for controlling AV devices

from flask import Flask, make_response
#import user
#import json
import directv

dtv = directv.DirecTV("192.168.88.253")
app = Flask(__name__)

def check_key(key):
        if key=='SOMESORTOFFNORDKEYHASH':
		return True
	else:
		return False

@app.route('/', methods=['GET'])
def index():
	key_check = check_key(request.args.get('key'))
	if key_check:
                return jsonify({'name':'Petraberg AV System','location':'Minneapolis, MN'})
        else:
                return jsonify({'error':'Invalid Key'})

@app.route('/dtv/key/<key>', methods=['GET'])
def dtv_key(key):
	key_check = check_key(request.args.get('key'))
	if key_check:
		dtv.sendkey(key,'keyPress')
                return jsonify({'keyPress':key})
	else:
                return jsonify({'error':'Invalid Key'})

@app.route('/dtv/chan/<chan>', methods=['GET'])
def dtv_chan(chan):
	key_check = check_key(request.args.get('key'))
	if key_check:
		dtv.sendchan(chan,'0')
                return jsonify({'channel':chan})
	else:
                return jsonify({'error':'Invalid Key'})

@app.errorhandler(404)
def not_found(error):
	key_check = check_key(request.args.get('key'))
	if key_check:
                return make_response(jsonify({'error': 'Not found'}), 404)
        else:
                return jsonify({'error':'Invalid Key'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
