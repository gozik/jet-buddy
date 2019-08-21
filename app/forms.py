from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, AnyOf

class TransactionForm(FlaskForm):
    allowed_categories = ['food', 'drinks', 'rent']

    value = DecimalField('value', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired(), AnyOf(allowed_categories)])
    date = DateTimeField('DateTime', validators=[DataRequired()])
    submit = SubmitField('Add')