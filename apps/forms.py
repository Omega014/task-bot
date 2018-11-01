from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import InputRequired


class QuestionForm(FlaskForm):
    id = HiddenField()
    title = StringField('Question',  [InputRequired()])
