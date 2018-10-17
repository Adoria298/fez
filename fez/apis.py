from flask import Flask, jsonify
from flask_restful import Resource, reqparse
 
messages = []

class Messages(Resource):

	def get(self):
		"""
		.. http:get:: /api/messages

   All messages

   **Example request**:

   .. sourcecode:: http

      GET /api/messages HTTP/1.1
      Host: localhost:5000
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      [
        {
          "name": "Lorem ipsum dolor",
		  "text": "sit amet consectetur adipiscing elit,",
		  "id": 0
        },
        {
          "name": "urna consequat felis ",
		  "text": "vehicula class ultricies mollis dictumst, aenean non a in donec nulla. ",
		  "id": 0
        }
      ]
		"""
		return messages, 200

	def post(self):
		"""
		.. http:post:: /api/messages

   All messages

   **Example request**:

   .. sourcecode:: http

      GET /api/messages HTTP/1.1
      Host: localhost:5000
      Accept: application/json
	  Content-Type: application/json
	  Data: {
		  "name": str,
		  "text": str
	  }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

	{
        "name": "Lorem ipsum dolor", // provided name
		"text": "sit amet consectetur adipiscing elit,", //provided text
		"id": 288 //generated id
    }
		"""
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
		"""
		.. http:put:: /api/messages

   All messages

   **Example request**:

   .. sourcecode:: http

      GET /api/messages HTTP/1.1
      Host: localhost:5000
      Accept: application/json
	  Content-Type: application/json
	  Data: {
		  "name": str,
		  "text": str,
		  "id": int //optional
	  }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

	{
        "name": "Lorem ipsum dolor", // provided name
		"text": "sit amet consectetur adipiscing elit,", //provided text
		"id": 288 //generated id, unless id provided
    }
		"""
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
		"""
		.. http:delete:: /api/messages

   All messages

   **Example request**:

   .. sourcecode:: http

      GET /api/messages HTTP/1.1
      Host: localhost:5000
      Accept: application/json
	  Content-Type: application/json
	  Data: {
		  "id": "all"
	  }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/text
	"Deleted all messages"

	:query id: either "all" or an integer id known to exist.
		"""
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()

		if (args["id"] == "all") or (args["id"] == None):
			messages = []
			return "Deleted all messages", 200
		else:
			messages.pop(args["id"])
			return "Deleted message %d." % args["id"], 200
