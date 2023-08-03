from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class SampleRegistrationForm(FlaskForm):
    OEM = StringField("OEM", validators=[DataRequired()])
    Program = StringField("Program", validators=[DataRequired()])
    Seat_Row = StringField("Seat Row", validators=[DataRequired()])
    Seat_Type = StringField("Seat Type", validators=[DataRequired()])
    submit = SubmitField('Register Seat Sample')


class TestRegistrationForm(FlaskForm):
    severity_choices = [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    label = StringField("Test Label", validators=[DataRequired()])
    Pulse = RadioField("Pulse Severity", choices=severity_choices)
    submit = SubmitField('Register Hardware Test')


class ResultForm(FlaskForm):
    NIC = FloatField("NIC", validators=[DataRequired()])
    Nkm = FloatField("Nkm", validators=[DataRequired()])
    rebound_velocity = FloatField("Rebound Velocity", validators=[DataRequired()])
    Fx_upper_neck = FloatField("Fx Upper Neck", validators=[DataRequired()])
    Fz_upper_neck = FloatField("Fz Upper Neck", validators=[DataRequired()])
    T1_acceleration = FloatField("T1 Acceleration", validators=[DataRequired()])
    time_head_contact = FloatField("Time Head Contact", validators=[DataRequired()])
    submit = SubmitField('Update Results!')
    cancel = SubmitField('Cancel')
