from flask import jsonify, redirect
from models import db, Participant

def get_all_participants(): 
  all_participants = Participant.query.all()
  results = [participant.as_dict() for participant in all_participants]
  return jsonify(results)

def get_participant(id):
  participant = Participant.query.get(id)                     
  if participant:           
    return jsonify(participant.as_dict())
  else:
    raise Exception(f'No participant at id: {id}')  

def create_participant(**form_kwargs):
  new_participant = Participant(**form_kwargs)
  db.session.add(new_participant)
  db.session.commit()
  return jsonify(new_participant.as_dict())

def update_participant(id, **update_values): 
  participant = Participant.query.get(id) 
  if participant:
    for key, value in update_values.items(): 
      setattr(participant, key, value) 
    db.session.commit()
    return jsonify(participant.as_dict())
  else:
    raise Exception(f'No participant at id: {id}')



def destroy_participant(id):
  participant = Participant.query.get(id)
  if participant:
    db.session.delete(participant)
    db.session.commit()
    return redirect('/participants')
  else:
    raise Exception(f'No participant at id: {id}')