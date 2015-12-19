# API app for controlling AV devices

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Petraberg AV Control Server'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
