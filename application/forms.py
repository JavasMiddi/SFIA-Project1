from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Customer, Order
from flask_login import current_user

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name: ',
            validators = [
                DataRequired(),
                Length(min=3, max=30) ])

    last_name = StringField('Last Name: ',
            validators = [
                DataRequired(),
                Length(min=2, max=30) ])

    email = StringField('Email: ',
        validators = [
            DataRequired(),
            Email() ])

    password = PasswordField('Password: ',
        validators = [
            DataRequired() ])

    confirm_password = PasswordField('Confirm Password: ',
        validators = [
            DataRequired(),
            EqualTo('password') ])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Customer.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email: ',
		validators=[
			DataRequired(),
			Email() ])

	password = PasswordField('Password: ',
		validators=[
			DataRequired() ])

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name: ',
            validators = [
                DataRequired(),
                Length(min=3, max=30) ])

    last_name = StringField('Last Name: ',
            validators = [
                DataRequired(),
                Length(min=2, max=30) ])
    email = StringField('Email: ',
        validators = [
            DataRequired(),
            Email() ])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Customer.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use!')

class PurchaseForm(FlaskForm):
    first_name = StringField('First Name: ',
            validators = [
                DataRequired(),
                Length(min=3, max=30) ])
    last_name = StringField('Last Name: ',
            validators = [
                DataRequired(),
                Length(min=2, max=30) ])
    email = StringField('Email: ',
        validators = [
            DataRequired(),
            Email() ])
    confirm_email = StringField('Confirm Email: ',
        validators = [
            DataRequired(),
            EqualTo('email') ])
   
    number = [
	('1'), ('2'), ('3'), ('4'), ('5') ]
   
    tickets = SelectField('Number of Tickets: ',
	choices=number,
	validators = [
	    DataRequired()
		])	       

    submit = SubmitField('Purchase')

    def validate_email(self, email):
        if email.data != current_user.email:
            raise ValidationError("Email didn't match!")
