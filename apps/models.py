import hashlib
from datetime import datetime
from apps.database import db

from flask_login import UserMixin


class BaseDateModel(db.Model):
    """ It is a base model add utime/ctime timestamp to anothermodelsi
    """
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class User(db.Model, BaseDateModel, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def get_id(self):
        return 1

    def get_auth_token(self):
        return unicode(hashlib.sha1(self.name + self.password).hexdigest())


class Question(db.Model, BaseDateModel):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)


class Answer(db.Model, BaseDateModel):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(255))


class Group(db.Model, BaseDateModel):

    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    channel = db.Column(db.String(255))

    def get_group(user):
        pass
