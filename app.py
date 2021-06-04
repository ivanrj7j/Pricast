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
app.secret_key = key_1
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    verified = db.Column(db.Integer)


def check_logged_in():
    if 'email' in session:
        print(session['email'])
        return True
    else:
        return False

def check_session(q):
    if session[q]:
        return session[q]
    else:
        return False

@app.route('/')
def hello():
    
    return render_template('index.html', title="Home Page", logged=check_logged_in())

@app.route('/login', methods=['GET', 'POST'])
def login():
   return render_template('login.html', title='Login', logged=check_logged_in())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   return render_template('signup.html', title='Signup', logged=check_logged_in())

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
   if request.method == 'POST':
       name = request.form.get('name')
       email = request.form.get('email')
       pass_encrypted = Fernet(key_2.encode()).encrypt(request.form.get('pass').encode()).decode()
       check_email = bool(User.query.filter_by(email=email).first())
       print(pass_encrypted)
       if check_email == False:
           data = User(username=name, email=email, password=pass_encrypted, verified=0)
           db.session.add(data)
           db.session.commit()
           session['email'] = email
           session['name'] = name
           return f"o"
       else:
           return "t"
       
       
   else:
        return redirect('/')

@app.route('/check_login', methods=['GET', 'POST'])
def check_login():
   if request.method == 'POST':
       email = request.form.get('email')
       password = request.form.get('pass')
       print(password)
       check_email = User.query.filter_by(email=email).first()
       if bool(check_email) == False:
           return "not found"
       password_encrypted = check_email.password.encode()
       password_decrypted = Fernet(key_2.encode()).decrypt(password_encrypted).decode()
       print(password_decrypted)
       if password == password_decrypted:
           session['email'] = email
           session['name'] = check_email.username
           return "success"
       else:
           return f"failed"
   else:
       return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=1234)