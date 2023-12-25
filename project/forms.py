from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class CreateBlogForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired(), Length(max=100)])
    body = TextAreaField("Content: ", validators=[DataRequired(), Length(min=10)])
    submit = SubmitField("Submit")

class CreateUserForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email(), Length(max=100)])
    name = StringField("Name: ", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Register")

class LoginUserForm(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Log in")