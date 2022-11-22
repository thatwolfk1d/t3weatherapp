"""Base render file for website"""
from flask import Flask,render_template
#from form import RegistrationForm,LoginForm,PasswordForm
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'c36e11ea44377df64f28a99fd99e98b8'

@app.route('/register')
def register():
    """Renders html on page load, and is home page"""
    return render_template("register.html")

@app.route('/login')
def login():
    """Renders html on page load, and is home page"""
    return render_template("login.html")

@app.route('/frame')
def frame():
    return render_template("frame.html")

