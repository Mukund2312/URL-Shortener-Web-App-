from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired , URL

class InputForm(FlaskForm):
    url_input = StringField("URL",validators=[ DataRequired() , URL()])
    submit = SubmitField("Shorten URL")