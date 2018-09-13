from flask import Blueprint
from requests import get, post, delete as rget, rpost, rdelete
import markdown
from . import MESSAGES_API_URL

frontend_bp = Blueprint('flask_messenger_frontend', __name__, template_folder='templates')

def message_format(message):
	markdown.markdown(message, 
						safe_mode='escape',
						lazy_ol=False)

@frontend_bp.route('/')
def index():
	messages = rget(MESSAGES_API_URL)
	messages.reverse()
	return render_template('view.html', messages=messages_copy, markdown_to_html_func=message_format)

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
