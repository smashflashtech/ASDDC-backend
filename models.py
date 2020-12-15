from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/asddc' 
db = SQLAlchemy(app)  

class Group(db.Model):
  __tablename__ = 'groups'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(10))

  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.name}"'

class Participant(db.Model):
  __tablename__ = 'participants'

  id = db.Column(db.Integer, primary_key=True)
  group_id = db.Column(db.Integer, db.ForeignKey('groups.id', ondelete='SET NULL')) # might want to ask what to do about this on delete setting.. although ill never delete a group
  dyad_L = db.Column(db.String(4), nullable=False)
  dyad_N = db.Column(db.Integer, nullable=False)
  remedial = db.Column(db.String(5))
  date_of_participation = db.Column(db.String(25), nullable=False)
  notes = db.Column(db.Text)

  def __repr__(self):
    return f'Participant(id={self.id}, groupId={self.group_id}, dyad="{self.dyad_L}{self.dyad_N}", remedial="{self.remedial}", date_of_participation="{self.date_of_participation}, notes="{self.notes}"'

  # def as_dict(self):
  #   return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Trial_Type(db.Model):
  __tablename__ = 'trial_types'

  id = db.Column(db.Integer, primary_key=True)
  trial_code = db.Column(db.String(25))

  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.trial_code}"'

class Set(db.Model):
  __tablename__ = 'sets'

  id = db.Column(db.Integer, primary_key=True)
  letter = db.Column(db.String(5))

  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.letter}"'

class Feedback(db.Model):
  __tablename__ = 'feedbacks' # weird

  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(25))

  def __repr__(self): 
    return f'Participant(id={self.id}, name="{self.code}"'
