import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    url = "http://127.0.0.1:5372/pong"
    requests.get(url=url, data="ping")
    data = request.data
    print(data)
    return 'ping'


if __name__ == '__main__':
    app.run(debug=True, port=4567)
