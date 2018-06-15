from flask import Flask
from flask_restful import Api, Resource, reqparse
from uuid import uuid4
app = Flask(__name__)
api = Api(app)

messages = []

class Message(Resource):
	
	def get(self, message=None):
		return messages, 200
	
	def post(self, message):
		parser = reqparse.RequestParser()
		parser.add_argument("name")
		args = parser.parse_args()
		
		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"]
			
		new_message = {
			"text": message,
			"name": name,
			"id": uuid4()
		}
		
		messages.append(new_message)
		return new_message, 201
		
	def put(self, message):
		parser = reqparse.RequestParser()
		parser.add_argument("name")
		parser.add_argument("id")
		args = parser.parse_args()
		
		if args["name"] == None:
			name = "Unknown"
		else:
			name = args["name"]
		
		for original_message in messages:
			if original_message["id"] == args["id"]: #if the user wants to update a message
				original_message["text"] = message
				original_message["name"] = args["name"]
				return original_message, 201
			
		new_message = {
			"text": message,
			"name": name,
			"id": uuid4()
		}
		
		messages.append(new_message)
		return new_message, 201
		
	def delete(self, message):
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()
		
		if args["id"] == None:
			for message in messages:
				messages.pop(message)
			return "Deleted all messages", 200
		else:
			for message in messages:
				if message["id"] == args["id"]:
					messages.pop(message)
					return "Deleted message with text {0}, and id {1} by user {2}".format(message["text"], message["id"], message["name"]), 200
@app.route('/')
def index():
	return str(messages)
				
api.add_resource(Message, "/messages/<string:message>")
if __name__ == '__main__':
	app.run(debug=True)
				
		
