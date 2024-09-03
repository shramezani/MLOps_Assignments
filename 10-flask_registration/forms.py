from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message="Username is required."),
        Length(min=3, message="Username must be at least 3 characters.")] 
    )

    email = StringField('Email', validators=[
        DataRequired(message="Email is required."),
         Email(message="Please enter a valid email address.")] 
    )
    password = PasswordField('Password', validators=[
        DataRequired(message="Password is required."), 
        Length(min=8, message="Password must be at least 8 characters long.")] 
    )
    confirm_password = PasswordField('Confirm Password', validators=[ 
        DataRequired(message="Please confirm your password."), 
        EqualTo('password', message='Passwords must match') ]
    )
    submit = SubmitField('Sign Up')