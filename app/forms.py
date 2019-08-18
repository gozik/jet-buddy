from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, AnyOf

class TransactionForm(FlaskForm):
    categories = ['food', 'drinks', 'rent']

    value = DecimalField('value', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired(), AnyOf(categories)])
    date = DateTimeField('DateTime', validators=[DataRequired()])
    submit = SubmitField('Add')