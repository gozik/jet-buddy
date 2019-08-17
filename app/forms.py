from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    value = DecimalField('value', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired()])
    date = DateTimeField('DateTime', validators=[DataRequired()])
    submit = SubmitField('Add')