from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

## when passed as a parameter to a template, an object of this class will be rendered as a regular HTML form
## with the additional restrictions specified for each field
class ResearchersForm(FlaskForm):
    researcher_ID = StringField(label = "ID", validators = [DataRequired(message = "ID is a required field.")])

    last_name = StringField(label = "Surname", validators = [DataRequired(message = "Surname is a required field.")])

    first_name = StringField(label = "Name", validators = [DataRequired(message = "Name is a required field.")])

    submit = SubmitField("Create")
