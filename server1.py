import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.route('/pong', methods=['GET', 'POST'])
def pong():
    url = "http://127.0.0.1:4567/ping"
    requests.get(url=url, data='pong')
    data = request.data
    print(data)
    return 'pong'


if __name__ == '__main__':
    app.run(debug=True, port=5372)
