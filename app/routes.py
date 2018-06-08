from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/api/v1/') # for GET
def api():
	return "API online"
