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
  print(data)
  return jsonify(dct=data)