from .frontend import frontend_bp
from .apis import api_bp

from flask import Flask
from flask_restplus import Api

import os

def create_app():
	"""
	fez app factory.
	
	No Parameters.
	Returns instance of flask.Flask().
	"""
	app = Flask("fez")
	
	app.secret_key = os.urandom(16)

	app.register_blueprint(api_bp)
	app.register_blueprint(frontend_bp)

	return app
