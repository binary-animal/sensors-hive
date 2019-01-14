import json
import requests
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from backend import backend, db
from backend.forms import LoginForm, RegistrationForm
from backend.models import User, Token
from config import Config

@backend.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'
    return response

@backend.route('/')
@backend.route('/index')
@login_required
def index():
    sensors = [{'id': 'sensor1', 'Temperature': '39.2', 'Humidity': '44'}, {'id': 'sensor2', 'Temperature': '22', 'Humidity': '21'}]
    res = ""
    for sensor in sensors:
        res += "Sensor: %s<br>Temperature: %s<br>Humidity: %s<br>"%(sensor['id'], sensor['Temperature'], sensor['Humidity'])

    return res
    # return render_template('index.html', title='Home', sensors_list=sensors)


@backend.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():  # if GET it False
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

    return render_template('login.html', form=form)


@backend.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@backend.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@backend.route('/api/login', methods=['POST'])  # for backward compatibility
@backend.route('/api/v1/login', methods=['POST'])
def login_v1():
    data = json.loads(request.data.decode('utf8'))
    user = User.query.filter_by(username=data['login']).one_or_none()
    if user is None:
        return json.dumps({ "status": "ERROR", "error_msg": "Login doesn't exist"})
    print(user.check_password(data['password']))
    if not user.check_password(data['password']):
        # need log it to analyze logs for ban bruteforcers
        return json.dumps({ "status": "ERROR", "error_msg": "Password wrong"})

    tknstr = Config.SECRET_KEY + data['login'] + data['password']
    token = Token(user_id=user.id)
    token.generate(tknstr)
    db.session.add(token)
    db.session.commit()
    res = {"id": str(user.id), "token": token.token}
    return json.dumps({ "status": "OK", "data": res})

@backend.route('/api/logout', methods=['POST'])
@backend.route('/api/v1/logout', methods=['POST'])
def logout_v1():
    data = json.loads(request.data.decode('utf8'))
    print(data)
    token = Token.query.filter_by(token=data['token']).one_or_none()
    if token is None:
        return json.dumps({ "status": "ERROR", "error_msg": "No token"})
    db.session.delete(token)
    db.session.commit()
    return json.dumps({ "status": "OK", "data": {}})


@backend.route('/api/v1/newtoken', methods=['POST'])
def newtoken_v1():
    data = json.loads(request.data.decode('utf8'))
    print(data)
    token_old = Token.query.filter_by(token=data['token']).one_or_none()
    if token_old is None:
        return json.dumps({ "status": "ERROR", "error_msg": "Wrong token"})

    tknstr = Config.SECRET_KEY + data['token']
    token_new = Token(user_id=token_old.user_id)
    token_new.generate(tknstr)

    db.session.delete(token_old)
    db.session.add(token_new)
    db.session.commit()

    return json.dumps({ "status": "OK", "data": { "token": token_new.token}})


@backend.route('/<path:path>')
def static_file(path):
    print(path)
    return backend.send_static_file(path)
