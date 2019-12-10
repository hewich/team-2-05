from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError


class LoginForm(FlaskForm):
    """Form Validation with WTForm.

        Arg: We define a user LoginForm which ask the user to enter their user name and password.
        This classes are represented by the WTForm package.

        Return: A Login Form.

        """
    username = StringField('User Name')
    password = PasswordField('Password')
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    """Form Validation with WTForm.

        Arg: We define a User RegisterForm which ask the user to enter their first name, last name, username, email,
        security question and password.
        This classes are represented by the WTForm package.

        Return: A Registration Form.

        """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    question = PasswordField('Secret Question', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TaskForm(FlaskForm):
    """Form Validation with WTForm.

        Arg: We define a User TaskForm which ask the user to enter a task name and description.

        Return: A Task Form.

        """
    task_name = StringField('Task Name')
    description = StringField('Description')
    submit = SubmitField('Submit')
    yes = SubmitField('Yes')


class ForgotForm(FlaskForm):
    """Form Validation with WTForm

    Arg: We define a User ForgotForm which ask the user to enter their user name, security question and the new reset
    password.

    Return: A Forgot Form.

"""
    username = StringField('User Name')
    question = PasswordField('Secret Question')
    reset_password = PasswordField('Password')
    reset = SubmitField('Reset')
