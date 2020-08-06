from application import db
from application.models import Customer, Artist, timeSlot, Order

db.drop_all()
db.create_all()

