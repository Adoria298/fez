# API declaration
from flask import Blueprint, jsonify
from flask_restplus import Api, Resource, reqparse

from .internal_messages import *

api_bp = Blueprint('fez_rest_apis', __name__, url_prefix='/api')

api = Api(api_bp, version='0.2.0', title='Fez API')

@api.route('/messages/')
class Messages(Resource):
	
	@api.response(200, 'JSON array of all messages returned')
	def get(self):
		"""
Returns all messages as a JSON array.
		"""
		return jsonify(get_messages()), 200

	@api.response(201, 'New JSON message returned')
	def post(self):
		"""
Creates a new message, consisting of the provided name and message.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("name", type=str, help="Name of user sending message.")
		parser.add_argument("text", type=str, help="Message user wants to send.")
		args = parser.parse_args()

		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"]

		text = args["text"]

		new_message = create_message(name, text)
		
		return jsonify(new_message), 201
	
	@api.response(201, 'Created or updated JSON message returned')
	def put(self):
		"""
Updates or creates a message. id parameter is optional.
If id provided:
	Updates the message with that id, with a new name/message. Both must be provided.
Otherwise:
	Creates a new message, same as POST method.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("name")
		parser.add_argument("id")
		parser.add_argument("text")
		args = parser.parse_args()

		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"]

		text = args["text"]

		new_message = update_message(args["id"], name, text)		
		return jsonify(new_message), 201
	
	@api.response(201, 'Deleted specified message.')
	def delete(self):
		"""
Deletes a specified message.
If id parameter is "all", deletes every message.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()

		delete_message(args["id"])
		return 201
