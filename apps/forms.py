from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired


class QuestionForm(FlaskForm):
    is_delete = BooleanField()
    title = StringField('Question',  [InputRequired()])
