from flask import Blueprint, render_template, request

#requests
from requests import get as rget
from requests import post as rpost
from requests import delete as rdelete

import markdown

from .constants import MESSAGES_API_URL

frontend_bp = Blueprint('fez_frontend', __name__, template_folder='templates')

def message_format(message):
	markdown.markdown(message, 
						safe_mode='escape',
						lazy_ol=False)

@frontend_bp.route('/')
def index():
	messages_response = rget(MESSAGES_API_URL)
	messages = []
	try:
		messages = messages_response.json()
		messages.reverse()
	except simplejson.errors.JSONDecoderError: #no messages
		messages = []
	except Exception as e:
		messages = [{"name": "System", "text": e, "id": 0}]
	finally:
		return render_template('view.html', messages=messages, markdown_to_html_func=message_format)

@frontend_bp.route('/about')
def about():
	return render_template('about.html')

@frontend_bp.route('/handle_data', methods=['POST'])
def handle_data():
	text = request.form["text"]
	name = request.form["name"]

	rpost(url=MESSAGES_API_URL, data={"name": name, "text": text})

	return index()

@frontend_bp.route('/handle_refresh', methods=['POST'])
def handle_refresh():
	return index()

@frontend_bp.route('/delete/<id>')
def delete(id):
	rdelete(url=MESSAGES_API_URL, data={"id": id})
	return index()
