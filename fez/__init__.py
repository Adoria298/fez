from .frontend import frontend_bp
from .apis import Messages
from flask import Flask
from flask_restful import Api

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
