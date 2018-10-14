from flask import Flask, jsonify
from flask_restful import Resource, reqparse
 
messages = []

class Messages(Resource):

	def get(self):
		return messages, 200

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument("name")
		parser.add_argument("text")
		args = parser.parse_args()

		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"][:70]

		text = args["text"][:140]

		new_message = {
			"text": text,
			"name": name,
			"id": len(messages)
		}

		messages.append(new_message)
		print(new_message)
		return new_message, 201

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument("name")
		parser.add_argument("id")
		parser.add_argument("text")
		args = parser.parse_args()

		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"][:70]

		text = args["text"][:140]

		if messages[args["id"]]: #if the user wants to update a message
			original_message = args["id"]
			original_message["text"] = text
			original_message["name"] = args["name"]
			return original_message, 201

		new_message = {
			"text": text,
			"name": name,
			"id": len(messages)
		}

		messages.append(new_message)
		print(new_message)
		return new_message, 201

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()

		if (args["id"] == "all") or (args["id"] == None):
			messages = []
			return "Deleted all messages", 200
		else:
			messages.pop(args["id"])
			return "Deleted message %d." % args["id"], 200
