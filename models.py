from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship #D
# from sqlalchemy.ext.declarative import declarative_base #D

# Base = declarative_base() #D

app = Flask(__name__) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/asddc' 
db = SQLAlchemy(app)  

class Group(db.Model):
  __tablename__ = 'groups'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(10))
  #Relation - one to many
  participants = db.relationship('Participant') #D

  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.name}"'




class Participant_Trial_Type(db.Model): #D
  __tablename__='participants_trial_types'
  id = db.Column(db.Integer, primary_key=True)
  participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))#D do i need primary key true here?
  trial_type_id = db.Column(db.Integer, db.ForeignKey('trial_types.id'))#D do i need primary key true here?
  position = db.Column(db.String(10))
  color = db.Column(db.String(10))
  value = db.Column(db.String(15))
  block_code = db.Column(db.String(25))
  feedback = db.Column(db.Boolean)
  trial_type = db.relationship('Trial_Type', back_populates='participant')#D 
  participant = db.relationship("Participant", back_populates='trial_type')#D
  def __repr__(self):
    return f'Response(id={self.id}, participant_id={self.participant_id}, trial_type_id="{self.trial_type_id}", position="{self.position}", color="{self.color}", value="{self.value}", block_code="{self.block_code}", cumulative_corrects="{self.cumulative_corrects}"'
  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Participant(db.Model):
  __tablename__ = 'participants'
  id = db.Column(db.Integer, primary_key=True)
  group_id = db.Column(db.Integer, db.ForeignKey('groups.id', ondelete='SET NULL')) # might want to ask what to do about this on delete setting.. although ill never delete a group
  dyad_L = db.Column(db.String(4), nullable=False)
  dyad_N = db.Column(db.Integer, nullable=False)
  remedial = db.Column(db.String(5))
  date_of_participation = db.Column(db.String(25), nullable=False)
  notes = db.Column(db.Text)
  #relations (belongs to one)
  group = db.relationship('Group', back_populates='participants') #D
  #Many to one TO association table
  trial_type = db.relationship('Participant_Trial_Type', back_populates='participant') #D
  def __repr__(self):
    return f'Participant(id={self.id}, groupId={self.group_id}, dyad="{self.dyad_L}{self.dyad_N}", remedial="{self.remedial}", date_of_participation="{self.date_of_participation}, notes="{self.notes}"'
  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Trial_Type(db.Model):
  __tablename__ = 'trial_types'
  id = db.Column(db.Integer, primary_key=True)
  trial_code = db.Column(db.String(25))
  #one to many to association table
  participant = db.relationship('Participant_Trial_Type', back_populates='trial_type') #D
  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.trial_code}"'

# trial_types_sets = db.Table(
#   'trial_types_sets',
#   db.Column('trial_type_id', db.Integer, db.ForeignKey('trial_types.id'), primary_key=True), # M
#   db.Column('set_id', db.Integer, db.ForeignKey('sets.id'), primary_key=True)                 #M
# )

# class Set(db.Model):
#   __tablename__ = 'sets'
#   id = db.Column(db.Integer, primary_key=True)
#   letter = db.Column(db.String(5))
#   def __repr__(self): 
#     return f'Participant(id={self.id}, name="{self.letter}"'

# feedbacks_sets = db.Table(
#   'feedbacks_sets',
#   db.Column('feedback_id', db.Integer, db.ForeignKey('feedbacks.id'), primary_key=True), # M
#   db.Column('set_id', db.Integer, db.ForeignKey('sets.id'), primary_key=True)                 #M
# )

# trial_types_feedbacks = db.Table(
#   'trial_types_feedbacks',
#   db.Column('trial_type_id', db.Integer, db.ForeignKey('trial_types.id'), primary_key=True), # M
#   db.Column('feedback_id', db.Integer, db.ForeignKey('feedbacks.id'), primary_key=True)                 #M
# )

# class Feedback(db.Model):
#   __tablename__ = 'feedbacks' # weird
#   id = db.Column(db.Integer, primary_key=True)
#   code = db.Column(db.String(25))
#   def __repr__(self): 
#     return f'Participant(id={self.id}, name="{self.code}"'
