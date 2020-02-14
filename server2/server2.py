import requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    data = request.data
    print(data)
    url = "http://127.0.0.1:8080/second"
    requests.get(
        url=url, json='{"url" : "http://127.0.0.1:4567/ping", "data" : "ping"}')
    return 'ping'


if __name__ == '__main__':
    app.run(debug=True)
