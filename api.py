from flask import (
  Flask, jsonify, request, render_template, url_for, json
)
from models import app, Participant
from crud.participant_crud import (get_all_participants, get_participant, create_participant, update_participant, destroy_participant)

from flask_cors import CORS
import os


#Middleware?
CORS(app)
@app.errorhandler(Exception)
def unhandled_exception(e):    
  app.logger.error(f'Unhandled Exception: {e}')
  message_str = e.__str__()
  return jsonify(message=message_str.split(':')[0])


#Participant Crud
@app.route('/participants', methods=['GET', 'POST'])
def create_get_participant():
  if request.method == 'GET':
    return get_all_participants()
  if request.method == 'POST':
    return create_participant(**request.getjson()) 

#IDK
@app.route('/', methods=['GET'])
def showjson():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'test.json')
  data = json.load(open(json_url))
  return jsonify(message=data)
  # return jsonify(message='')

@app.route('/amts', methods=['GET'])
def amts():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'aMTS.json')
  data = json.load(open(json_url))
  return jsonify(amts=data)

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

@app.route('/instructions/<phase>', methods=['GET'])
def instructions(phase):
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', f"i_{phase}.json")
  data = json.load(open(json_url))
  return jsonify(instructions=data)

@app.route('/nonamts/<set>', methods=['GET'])
def namts(set):
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', f"set{set}.json")
  data = json.load(open(json_url))
  return jsonify(namts=data) 

@app.route('/npst', methods=['GET'])
def npst():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'novelPST.json')
  data = json.load(open(json_url))
  return jsonify(npst=data)

@app.route('/psvott', methods=['GET'])
def psvott():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'psvotTact.json')
  data = json.load(open(json_url))
  return jsonify(psvott=data)

@app.route('/psvotiv', methods=['GET'])
def psvotIV():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'psvotIV.json')
  data = json.load(open(json_url))
  return jsonify(psvotiv=data)

@app.route('/psvotps', methods=['GET'])
def psvotPS():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'psvotPS.json')
  data = json.load(open(json_url))
  return jsonify(psvotps=data)

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

@app.route('/tp', methods=['GET'])
def tp():
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT,'stimuli/', 'tp.json')
  data = json.load(open(json_url))
  return jsonify(tp=data)

