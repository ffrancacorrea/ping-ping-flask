import requests
import json
import time
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

first_data = ""
second_data = ""
first_url = ""
second_url = ""


def call(first_data, second_data, first_url, second_url):
    print(first_url)
    print(first_data)
    print(second_url)
    print(second_data)

    time.sleep(2)
    requests.get(url=str(first_url), data=str(second_data))
    time.sleep(2)
    requests.get(url=str(second_url), data=str(first_data))


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello</h1>'


@app.route('/first', methods=['GET', 'POST'])
def first():
    res = json.loads(request.json)
    global first_data
    first_data = res['data']
    global first_url
    first_url = res['url']

    if first_data != '':
        if second_data != '':
            print('ok')
            call(first_data, second_data, first_url, second_url)
    return 'first'


@app.route('/second', methods=['GET', 'POST'])
def second():
    res = json.loads(request.json)
    global second_data
    second_data = res['data']
    global second_url
    second_url = res['url']

    if first_data != '':
        if second_data != '':
            print('ok')
            call(first_data, second_data, first_url, second_url)

    return 'second'


if __name__ == '__main__':
    app.run(debug=True,)
