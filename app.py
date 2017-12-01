from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view/<messages>')
def hello(messages):
    return render_template('view.html', messages=messages)

@app.route('/handle_data', methods=['POST'])
def handle_data():
	print(request.form['message'])
	request.form['message']
	message = request.form['message']
	if len(message) < 10:
		message = '<div>' + message
		message += '</div>'
		messages.append(message)		
	else:
		return hello(messages)
	return hello(messages)

@app.route('/handle_refresh', methods=['POST'])	
def handle_refresh():
	return hello(messages)
	
def clear_messages():
	messages = []
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
