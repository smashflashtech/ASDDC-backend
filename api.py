from flask import (
  Flask, jsonify, request, render_template, url_for, json
)
from models import app
from flask_cors import CORS
import os

#Middleware?
CORS(app)

#IDK
@app.route('/', methods=['GET'])
def showjson():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'test.json')
  data = json.load(open(json_url))
  return jsonify(message=data)
  # return jsonify(message='')


@app.route('/dct', methods=['GET'])
def dct():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'dct.json')
  data = json.load(open(json_url))
  return jsonify(dct=data)

@app.route('/evott', methods=['GET'])
def evott():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'evotTact.json')
  data = json.load(open(json_url))
  return jsonify(evott=data)

@app.route('/evotiv', methods=['GET'])
def evotiv():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'evotIV.json')
  data = json.load(open(json_url))
  return jsonify(evotiv=data)

@app.route('/npst', methods=['GET'])
def npst():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'novelPST.json')
  data = json.load(open(json_url))
  return jsonify(npst=data)

@app.route('/sd', methods=['GET'])
def sd():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'sDisc.json')
  data = json.load(open(json_url))
  return jsonify(sd=data)

@app.route('/sp', methods=['GET'])
def sp():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'sPair.json')
  data = json.load(open(json_url))
  return jsonify(sp=data)

@app.route('/tat', methods=['GET'])
def tat():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'talkAloud.json')
  data = json.load(open(json_url))
  return jsonify(tat=data)

@app.route('/tsf', methods=['GET'])
def tsf():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'tsf.json')
  data = json.load(open(json_url))
  return jsonify(tsf=data)