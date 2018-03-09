from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
messages = []
loggedIn = False

#pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view/<messages>')
def hello(messages):
    messages_reversed = messages.copy()  #copied to prevent a confusing order.
    messages_reversed.reverse()
    print(messages_reversed)
    print(messages)
    return render_template('view.html', messages=messages_reversed)

@app.route('/login')
def login_page():
	return render_template('login.html')

@app.route('/admin')
def admin_page():
	if loggedIn:
		return render_template('admin.html')
	else:
		return render_template('not_admin.html')

@app.route('/about')
def about_page():
	return render_template('about.html')


#handlers
@app.route('/handle_data', methods=['POST'])
def handle_data():
	request.form['message']
	message = request.form['message']
	if len(message) < 140:
		messages.append(message)
		print(message)
	else:
		return hello(messages)
	return hello(messages)

@app.route('/handle_refresh', methods=['POST'])
def handle_refresh():
	return hello(messages)

@app.route('/handle_login')
def handle_login():
	loggedIn = True
	return hello(messages)

#admin function
@app.route('/clear_messages')
def clear_messages():
	for i in messages:
		messages.pop()
	return hello(messages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
