from flask import render_template
from backend import backend 
from backend import common

@backend.route('/')
@backend.route('/index')
def index():
    sensors = [{ 'id': 'sensor1', 'Temperature': '39.2', 'Humidity': '44' }, { 'id': 'sensor2', 'Temperature': '22', 'Humidity': '21' }]
    res = ""
    for sensor in sensors:
    	res+="Sensor: %s<br>Temperature: %s<br>Humidity: %s<br>"%(sensor['id'], sensor['Temperature'], sensor['Humidity'])

    return res
    # return render_template('index.html', title='Home', sensors_list=sensors)

@backend.route('/api/v1/') # for GET
def api():
    api()
    return "API online"
