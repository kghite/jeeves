# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import google_api
import jeeves

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
    response = 'Jeeves will respond here'
    command = 'Jeeves will respond here'
    if request.method == 'POST':
        command = request.form['text']
        command = command.lower()
        response = str(jeeves.respond_to_command(command))
        print(response)
        return render_template('main.html', command = response)
    return render_template('main.html', command = command)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)