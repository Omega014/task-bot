from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class QuestionForm(FlaskForm):
    title = StringField('Question',  [InputRequired()])
