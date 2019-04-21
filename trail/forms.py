from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired, EqualTo
from trail.models import User 



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('The Username is already taken. Please choose another one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddBook(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    ISBN = StringField('ISBN', validators=[DataRequired()])
    authors = StringField('Author', validators=[DataRequired()])
    rating = IntegerField('Book Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


class SearchBook(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()])
    submit = SubmitField('Search for Books')