from .frontend import frontend_bp
from .apis import api_bp
from flask import Flask
from flask_restplus import Api

def create_app():
	"""
	fez app factory.
	
	No Parameters.
	Returns instance of flask.Flask().
	"""
	app = Flask("fez")
	
	app.register_blueprint(api_bp)
	app.register_blueprint(frontend_bp)

	return app
