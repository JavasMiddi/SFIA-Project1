from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Customer(db.Model, UserMixin):
	CustomerID = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(250), nullable=False)

class Artist(db.Model, UserMixin):
	ArtistID = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	genre = db.Column(db.String(30), nullable=False)
	Type = db.Column(db.String(30), nullable=False) 

class timeSlot(db.Model, UserMixin):
	ActNo = db.Column(db.Integer, primary_key=True)
	ArtistID = db.Column(db.Integer, db.ForeignKey('Artist.ArtistID'), 
		nullable=False)
	startTime = db.Column(db.Integer, nullable=False)
	endTime = db.Column(db.Integer, nullable=False)
	Day = db.Column(db.String(9), nullable=False)

class Order(db.Model, UserMixin):
	OrderID = db.Column(db.Integer, primary_key=True)
	CustID = db.Column(db.Integer, db.ForeignKey('Customer.CustomerID'), 
		nullable=False)
	email = db.Column(db.String(150), db.ForeignKey('Customer.email'), 
		nullable=False)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

