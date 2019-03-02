from flask import Blueprint, render_template, request, session
import markdown
import json

from .constants import MESSAGES_API_URL
from .apis.internal_messages import get_messages, create_message, delete_message

frontend_bp = Blueprint('fez_frontend', __name__, template_folder='templates')

names = ["Fez"] # frontend only

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

	if not session.get("name", False):
		session["name"] = "User" + str(len(names))

	return render_template('view.html', messages=messages, markdown_to_html_func=message_format, username=session["name"])

@frontend_bp.route('/about')
def about():
	return render_template('about.html')

@frontend_bp.route('/change_name')
def change_name():
	return render_template('change_name.html')

@frontend_bp.route('/handle_name_change', methods=['POST'])
def handle_name_change():
	new_name = request.form["new_name"]

	if new_name not in names:
		session["name"] = new_name
		names.append(new_name)
	else:
		create_message("Fez", session["name"] + " tried to be renamed "  + new_name + ".")
	
	return index()

@frontend_bp.route('/handle_data', methods=['POST'])
def handle_data():
	text = request.form["text"]
	name = session["name"]

	create_message(name, text)

	return index()

@frontend_bp.route('/handle_refresh', methods=['POST'])
def handle_refresh():
	return index()

@frontend_bp.route('/delete/<id>')
def delete(id):
	delete_message(id)
	return index()
