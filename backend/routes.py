import json
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from backend import backend, db
from backend.forms import LoginForm, RegistrationForm
from backend.models import User, Token
from config import Config


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


@backend.route('/api/login', methods=['GET', 'POST'])  # for backward compatibility
@backend.route('/api/v1/login', methods=['GET', 'POST'])
def login_v1():
    data = json.loads(request.data.decode('utf8'))
    s = json.dumps(data, indent=4, sort_keys=True)
    print(s)
    user = User.query.filter_by(username=data['login']).first()
    print(user.id)
    tknstr = Config.SECRET_KEY + data['login'] + data['password']
    token = Token(user_id=user.id)
    token.generate(tknstr)
    db.session.add(token)
    db.session.commit()
    res = {"id": user.id, "token": token.token}
    return render_template('login.json', data=res)
