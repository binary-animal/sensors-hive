## How to start sensor-hive on developer environment

### Preparing Environment
```
git clone https://github.com/binary-animal/sensors-hive.git
pip3 install -r requirements.lst
npm install
npm run-script build
```

### Initialize database
```
FLASK_APP=sensors-hive.py flask db migrate 
FLASK_APP=sensors-hive.py flask db upgrade 
```

### Run stand alone server
```
./run_standalone.sh
```