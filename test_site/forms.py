from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from test_site.models import Profile

class ProfileForm(FlaskForm):
    username=StringField('Username', validators = [DataRequired()])
    language=StringField('Language', validators = [DataRequired()])
    age=IntegerField('Age',validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = Profile.query.filter_by(username=name_.data).first()    
        if user:
            raise ValidationError('This name has already been used. Please enter a different name')
