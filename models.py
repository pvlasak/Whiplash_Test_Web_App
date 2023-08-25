from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, passwd):
        self.password_hash = generate_password_hash(passwd)
        return self.password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    oem = db.Column(db.String(80), index=True, unique=False)
    program = db.Column(db.String(80), index=True, unique=False)
    seat_row = db.Column(db.Integer, index=True, unique=False)
    seat_type = db.Column(db.String(120), index=True, unique=False)
    tests = db.relationship('Test', backref='sample', lazy='dynamic')


class Pulse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    severity = db.Column(db.String(64), index=True, unique=True)
    comment = db.Column(db.String(256), index=False, unique=False)
    tests = db.relationship("Test", backref='pulse_severity', lazy='dynamic')


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(128), index=True, unique=False)
    pulse_id = db.Column(db.Integer, db.ForeignKey('pulse.id'))
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
    result_id = db.relationship('Result', backref='test', uselist=False, cascade='all, delete, delete-orphan')


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backset = db.Column(db.Float, unique=False)
    height = db.Column(db.Float, unique=False)
    NIC = db.Column(db.Float, index=False, unique=False)
    Nkm = db.Column(db.Float, index=False, unique=False)
    rebound_velocity = db.Column(db.Float, index=False, unique=False)
    Fx_upper_neck = db.Column(db.Float, index=False, unique=False)
    Fz_upper_neck = db.Column(db.Float, index=False, unique=False)
    T1_acceleration = db.Column(db.Float, index=False, unique=False)
    time_head_contact = db.Column(db.Float, index=False, unique=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))

    def __repr__(self):
        return 'Test result id = {}'.format(self.id)
