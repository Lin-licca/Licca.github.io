from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from datetime import datetime

app = Flask(__name__, static_folder = 'statics')
app.secret_key = 'aou.3au4a83'

@app.route('/')
def hi():
    return render_template('home.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/interests')
def interests():
    return render_template('interests.html')

@app.route('/self')
def self():
    return render_template('self.html')

@app.route('/thank')
def thank():
    return render_template('thank.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')

if __name__ == '__main__':
    app.run()