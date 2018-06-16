from flask import Flask
from flask_restful import Api, Resource, reqparse
from uuid import uuid4

app = Flask(__name__)
api = Api(app)

messages = []

class Message(Resource):
	
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
			name = args["name"]

		text = args["text"]
			
		new_message = {
			"text": text,
			"name": name,
			"id": str(uuid4())
		}
		
		messages.append(new_message)
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
			name = args["name"]

		text = args["text"]
		
		for original_message in messages:
			if original_message["id"] == args["id"]: #if the user wants to update a message
				original_message["text"] = text
				original_message["name"] = args["name"]
				return original_message, 201
			
		new_message = {
			"text": text,
			"name": name,
			"id": str(uuid4())
		}
		
		messages.append(new_message)
		return new_message, 201
		
	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()
		
		if args["id"] == "all":
			for message in messages:
				messages.pop(message)
			return "Deleted all messages", 200
		else:
			for index, message in enumerate(messages):
				if message["id"] == args["id"]:
					messages.pop(index)
					return "Deleted message {0}".format(message["id"]), 200
@app.route('/')
def index():
	return str(messages)
				
api.add_resource(Message, "/messages")
if __name__ == '__main__':
	app.run(debug=True)
				
		
