import hashlib
from datetime import datetime
from apps.database import db

from flask_login import UserMixin


class UserChannel(db.Model):

    __tablename__ = 'users_channels'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), primary_key=True)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    user = db.relationship('User')
    channel = db.relationship('Channel')


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    channels = db.relationship(
        'Channel',
        secondary=UserChannel.__tablename__,
        back_populates='users',
    )
    user_channel = db.relationship('UserChannel')

    def get_id(self):
        return 1

    def get_auth_token(self):
        return hashlib.sha1(self.name + self.password).hexdigest()


class Channel(db.Model):

    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    users = db.relationship(
        'User',
        secondary=UserChannel.__tablename__,
        back_populates='channels',
    )
    user_channel = db.relationship('UserChannel')

    @classmethod
    def get_channels(cls, user):
        return cls.query.filter(cls.id == user.id)


class Question(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class Answer(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(255))
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
