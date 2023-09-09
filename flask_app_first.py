from flask import Flask, redirect, url_for, request

app = Flask(__name__)
@app.route('/success/hello')

def success():
	return 'Hello %s' % value
	
@app.route('/login', methods=['POST', 'GET'])

def login():
	if request.method == 'POST':
		global value
		value = request.form['nm']
		return redirect(url_for('success'))
	else:
		user = request.args.get('nm')
		return redirect (url_for('success', name=user))
	
if __name__ == '__main__':
	app.run(debug=True)
