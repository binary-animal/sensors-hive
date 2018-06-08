from flask import render_template
from app import app
from app import common

@app.route('/')
@app.route('/index')
def index():
    sensors = { 'Temperature': '39.2', 'Humidity': '44' }
    for sensor in sensors:
    	pass

    return sensor.
    # return render_template('index.html', title='Home', sensors_list=sensors)

@app.route('/api/v1/') # for GET
def api():
    api()
    return "API online"
