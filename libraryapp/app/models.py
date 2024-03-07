import enum
from datetime import datetime, timedelta
from sqlalchemy import event
from sqlalchemy.sql import func

from .extensions import db

# class SexEnum(enum.Enum):
#     male = 'Male'
#     female = 'Female'
#     other = 'Other'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    # sex = db.Column(db.Enum(SexEnum), nullable=True)
    subscription = db.relationship('Subscription', uselist=False, back_populates='user')

    def __repr__(self):
        return f"<{self.f_name} {self.l_name}>"

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    date_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    valid_upto = db.Column(db.DateTime(timezone=True), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='subscription')

    def __repr__(self):
        return f"User: {self.user_id} | Date created: {self.date_created} | Valid Upto: {self.valid_upto} "

# @event.listens_for(Subscription, 'before_insert')
# def set_valid_upto_default(mapper, connection, target):
#     if target.date_created:
#         target.valid_upto = target.date_created + timedelta(days=12*30)
#     else:
#         # Handle the case when date is None (optional)
#         target.valid_upto = None

# event.listen(Subscription, 'before_update', set_valid_upto_default)

# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

#     def __str__(self):
#         return self.name

# class Genre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = 
#     name = db.Column() # Enum

#     def __repr__(self):
#         return f"{self.type} {self.name}"

# class Book(db.Model):
#     db.Column(db.Uuid, primary_key=True, default=uuid.uuid4)
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), nullable=False)
#     author = 
#     publisher = db.Column(db.String(50), nullable=False)
#     publish_date = db.Column(db.Date, nullable=True)

#     def __repr__(self):
#         return f"{self.genre_name}"

# class Borrow(db.Model):
#     pass
