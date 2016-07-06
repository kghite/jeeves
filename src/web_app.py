# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import google_api

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
    	print('Login post called')
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('main'))
    return render_template('index.html', error=error)

	
@app.route('/main', methods=['GET', 'POST'])
def main():
	command = 'command will appear here'
	if request.method == 'POST':
		command_input = request.form['text']
		command = command_input.upper()
		return render_template('main.html', command = command)
	return render_template('main.html', command = command)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)