from frontend import frontend_bp
from apis import api_bp
from flask import Flask

INDEX_URL = '0.0.0.0:5000'
API_URL = INDEX_URL + '/api'
MESSAGES_API_URL = API_URL + '/messages'

def create_app():
	"""
	flask-messenger app factory.
	
	No Parameters.
	Returns instance of flask.Flask().
	"""
	app = Flask("flask_messenger")
	
	app.register_blueprint(frontend_bp)
	
	return app
