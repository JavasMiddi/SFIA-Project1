from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Customer(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(250), nullable=False)

class Artist(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	genre = db.Column(db.String(30), nullable=False)
	type = db.Column(db.String(30), nullable=False) 
	slot = db.relationship('timeSlot', backref='artist', lazy=True)

class timeSlot(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	ArtistID = db.Column(db.Integer, db.ForeignKey('artist.id'), 
		nullable=False)
	startTime = db.Column(db.Integer, nullable=False)
	endTime = db.Column(db.Integer, nullable=False)
	Day = db.Column(db.String(9), nullable=False)

class Order(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	CustID = db.Column(db.Integer, db.ForeignKey('customer.id'), 
		nullable=False)
	email = db.Column(db.String(150), db.ForeignKey('customer.email'), 
		nullable=False)
	tickets = db.Column(db.Integer, nullable=False)
	custid = db.relationship("Customer", foreign_keys=[CustID])
	custemail = db.relationship("Customer", foreign_keys=[email])

@login_manager.user_loader
def load_user(id):
    return Customer.query.get(int(id))

