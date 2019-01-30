from datetime import datetime, timedelta
from backend import db
from backend.models import Sensor, SensorsGroup, NNSensorGroup, History

dt = datetime.utcnow();

for i in range(0, 10):
    event = History(sensor=0, value=i*100, time=dt+timedelta(hours=3*i))
    db.session.add(event)

db.session.commit()
