from os import environ
from foaas import fuck
from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

app = Flask(__name__)
slack_token = environ['SLACK_TOKEN']

@app.route("/slack/foaas", methods=['POST'])
def foaas():
    if 'token' not in request.form:
        abort(401)
    if request.form['token'] != slack_token:
        abort(401)

    resp = {}
    resp['response_type'] = 'in_channel'
    if request.form['text'] == '':
        resp['text'] = fuck.random(from_=request.form['user_name']).text
    else:
        resp['text'] = fuck.random(name=request.form['text'], from_=request.form['user_name']).text
    return jsonify(resp)
