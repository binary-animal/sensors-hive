from datetime import datetime
from backend import db
from backend import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tokens = db.relationship('Token', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    token = db.Column(db.String(140))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Token {} for user_id {}>'.format(self.token, self.user_id)

    def generate(self, str):
        self.token = generate_password_hash(str).split('$')[2]
        return self.token


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    model = db.Column(db.String(140))
    name = db.Column(db.String(140))
    description = db.Column(db.String(1000))
    units = db.Column(db.Integer)
    value = db.Column(db.String(50))
    max = db.Column(db.String(50))
    min = db.Column(db.String(50))


class SensorsGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(1000))


class NNSensorGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor = db.Column(db.Integer)
    group = db.Column(db.Integer)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
