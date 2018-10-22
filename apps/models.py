import hashlib
from datetime import datetime
from apps.database import db

from flask_login import UserMixin


class UserGroup(db.Model):

    __tablename__ = 'users_group'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    user = db.relationship('User')
    group = db.relationship('Group')

    @classmethod
    def get_group(cls, user):
        pass


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    group = db.relationship(
        'Group',
        secondary=UserGroup.__tablename__,
        back_populates='users',
    )
    user_group = db.relationship('UserGroup')

    def get_id(self):
        return 1

    def get_auth_token(self):
        return unicode(hashlib.sha1(self.name + self.password).hexdigest())


class Question(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
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


class Group(db.Model):

    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    channel = db.Column(db.String(255))
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    users = db.relationship(
        'User',
        secondary=UserGroup.__tablename__,
        back_populates='group',
    )
    user_group = db.relationship('UserGroup')

    @classmethod
    def get_group(cls, user):
        gronp = cls.query.filter(cls.id==user_id)
        return group
