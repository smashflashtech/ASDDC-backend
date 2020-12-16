from flask import jsonify, redirect
from models import db, Participant_Trial_Type, Trial_Type

def get_all_responses(): 
  all_responses = Participant_Trial_Type.query.all()
  results = [response.as_dict() for response in all_responses]
  return jsonify(results)

def create_response(trialcode, **form_kwargs):
  print(set)
  new_response = Participant_Trial_Type(
    trial_type_id = Trial_Type.query.filter_by(trial_code=trialcode).one().id,
    **form_kwargs)
  db.session.add(new_response)
  db.session.commit()
  return jsonify(new_response.as_dict())