# website/models.py
from .database import db
from flask_login import UserMixin

class Train(db.Model):
    train_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    train_name = db.Column(db.String(50))
    arrival_time = db.Column(db.Time)
    departure_time = db.Column(db.Time)

class Station(db.Model):
    station_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_name = db.Column(db.String(50))
    location = db.Column(db.String(50))

class Route(db.Model):
    route_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    start_station_id = db.Column(db.Integer, db.ForeignKey('station.station_id'))
    end_station_id = db.Column(db.Integer, db.ForeignKey('station.station_id'))
    distance = db.Column(db.Float)

class Passenger(db.Model):
    passenger_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    contact_number = db.Column(db.String(15))

class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    issue_date = db.Column(db.Date)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.passenger_id'))

class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.Integer)
    status = db.Column(db.String(50))
    booking_date = db.Column(db.Date)
    train_id = db.Column(db.Integer, db.ForeignKey('train.train_id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.ticket_id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    contact = db.Column(db.String(15))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))