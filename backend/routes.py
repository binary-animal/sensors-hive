from flask import render_template, flash, redirect, url_for
from backend import backend
from backend import common
from backend.forms import LoginForm


@backend.route('/')
@backend.route('/index')
def index():
    sensors = [{'id': 'sensor1', 'Temperature': '39.2', 'Humidity': '44'}, {'id': 'sensor2', 'Temperature': '22', 'Humidity': '21'}]
    res = ""
    for sensor in sensors:
        res += "Sensor: %s<br>Temperature: %s<br>Humidity: %s<br>"%(sensor['id'], sensor['Temperature'], sensor['Humidity'])

    # print(backend.config['SECRET_KEY'])
    return res
    # return render_template('index.html', title='Home', sensors_list=sensors)


@backend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # if GET it False
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@backend.route('/api/v1/') # for GET
def api():
    common.api()
    return "API online"
