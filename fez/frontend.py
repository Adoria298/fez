from flask import Blueprint, render_template, request
import markdown
import json

from .constants import MESSAGES_API_URL
from .apis.internal_messages import get_messages, create_message, delete_message

frontend_bp = Blueprint('fez_frontend', __name__, template_folder='templates')

def message_format(message):
	message = markdown.markdown(message, 
						safe_mode='escape',
						lazy_ol=False)
	return message

@frontend_bp.route('/')
@frontend_bp.route('/home')
def index():
	try:
		messages = get_messages()
		messages.reverse()
	except Exception as e:
		create_message("Fez", str(e))
	return render_template('view.html', messages=messages, markdown_to_html_func=message_format)

@frontend_bp.route('/about')
def about():
	return render_template('about.html')

@frontend_bp.route('/handle_data', methods=['POST'])
def handle_data():
	text = request.form["text"]
	name = request.form["name"]

	create_message(name, text)

	return index()

@frontend_bp.route('/handle_refresh', methods=['POST'])
def handle_refresh():
	return index()

@frontend_bp.route('/delete/<id>')
def delete(id):
	delete_message(id)
	return index()
