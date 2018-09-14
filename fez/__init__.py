from frontend import frontend_bp
from apis import Messages
from flask import Flask
from flask_restful import Api

INDEX_URL = '0.0.0.0:5000'
API_URL = INDEX_URL + '/api'
MESSAGES_API_URL = API_URL + '/messages'

def create_app():
	"""
	fez app factory.
	
	No Parameters.
	Returns instance of flask.Flask().
	"""
	app = Flask("fez")
	api = Api(app)
	
	api.add_resource(Messages, "/api/messages")
	
	app.register_blueprint(frontend_bp)
	
	return app
