from flask_wtf import FlaskForm
from wtforms import StringField


class QuestionForm(FlaskForm):
    title = StringField('Question')

