'''
Created on Nov 18, 2022

@author: franciscolopez
'''
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "create-secret-key"

db = SQLAlchemy(app)

class Users(db.Model):
    '''
    Users class creates Users table in database
    '''
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def register():
    '''
    Displays the Registration Page
    '''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
    
        # create new user with input from registration page
        new_user = Users(first_name, last_name, email, password=generate_password_hash(password, method='sha256'))    
        db.session.add(new_user)
        db.session.commit
        return "Success"
        
    return render_template('register.html')
   
if __name__ == '__main__':
    app.run()
