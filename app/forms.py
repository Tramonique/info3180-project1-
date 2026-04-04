from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired, MultipleFileField
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired(), NumberRange(min=1)])
    bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1)])
    currency = SelectField(
        'Currency',
        choices=[('JMD', 'JMD'), ('USD', 'USD'), ('CAD', 'CAD')],
        validators=[DataRequired()]
    )
    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only')
    ])
    images = MultipleFileField('Additional Images', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only')
    ])
    submit = SubmitField('Add Property')