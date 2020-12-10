from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/ASDDC' 
db = SQLAlchemy(app)  

