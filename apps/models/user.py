from datetime import datetime
from apps.database import db

from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    utime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def get_id(self):
        return 1
