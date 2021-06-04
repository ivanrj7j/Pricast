from __future__ import with_statement
import re
from flask import *
from flask_sqlalchemy import *
from cryptography.fernet import Fernet
from flask import sessions
# importing the libraries and packages needed 
app = Flask(__name__)
key_1 = ''
key_2 = ''
with open('hello.txt', 'r') as key:
    key_1 = key.read()

with open('bruh.txt', 'r') as content:
    key_2 = content.read()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# initialising the connection to the database 
app.secret_key = key_1
# initinalising the secret key for the app 
db = SQLAlchemy(app)
# initialising the database object 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    verified = db.Column(db.Integer)

# making the blueprint for user database 

def check_logged_in():
    if 'email' in session:
        # checking if 'email' is present in the session, which will decide if the user is
        # logged in or not 
        # returning true if the user is logged in 
        return True
    else:
        return False

def check_session(q):
    if session[q]:
        return session[q]
        # hooking up the session defined
    else:
        return False

@app.route('/')
def hello():
    # rendering the main page 
    return render_template('index.html', title="Home Page", logged=check_logged_in())

@app.route('/login', methods=['GET', 'POST'])
def login():
    # the login page, if the user is already logged in, this will redirect them to the 
    # main page, else this will let them log in
    if check_logged_in():
       return redirect('/')
    else:
       return render_template('login.html', title='Login', logged=check_logged_in())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # the signup page, if the user is already logged in, this will redirect them to the 
    # main page, else this will let them sign up
   if check_logged_in():
       return redirect('/')
   else:
       return render_template('signup.html', title='Signup', logged=check_logged_in())

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    # this will make a user sign up 
   if request.method == 'POST':
       name = request.form.get('name')
       email = request.form.get('email')
       pass_encrypted = Fernet(key_2.encode()).encrypt(request.form.get('pass').encode()).decode()
    #    getting the email, name and password 
       check_email = bool(User.query.filter_by(email=email).first())
    #    quering if the email already exists 
       
       if check_email == False:
           data = User(username=name, email=email, password=pass_encrypted, verified=0)
           db.session.add(data)
           db.session.commit()
        #    commiting the data to the database 
           session['email'] = email
           session['name'] = name
        #    making the sessions 
           return f"o"
       else:
           return "t"
       
       
   else:
        return redirect('/')

@app.route('/check_login', methods=['GET', 'POST'])
def check_login():
    # checks if the login info is true 
   if request.method == 'POST':
       email = request.form.get('email')
       password = request.form.get('pass')
    #    getting the request email and password 
       
       check_email = User.query.filter_by(email=email).first()
    #    quering the email from the database 
       if bool(check_email) == False:
           return "not found"
        #    if the email doesnt exists, this will return not found response 
       password_encrypted = check_email.password.encode()
    #    hooking up the password in the database and converting it into byte object 
       password_decrypted = Fernet(key_2.encode()).decrypt(password_encrypted).decode()
    #    decrypting the password in the db 
       
       if password == password_decrypted:
           session['email'] = email
           session['name'] = check_email.username
        #    if the password provided and the password in db decrypted matches, this let 
        # them log in
           return "success"
       else:
           return f"failed"
   else:
       return redirect('/')

@app.route('/logout')
def logout():
    if check_logged_in():
        session.pop('email', None)
        session.pop('name', None)
        return redirect('/')
    else:
        return redirect('/')
    # logs out the user only if the user is logged in 

if __name__ == '__main__':
    app.run(debug=True, port=1234)