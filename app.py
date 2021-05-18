from __future__ import with_statement
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



def check_session(q):
    if session[q]:
        return session[q]
    else:
        return False

@app.route('/')
def hello():
    
    return render_template('index.html', title="Home Page", logged=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
   return render_template('login.html', title='Login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   return render_template('signup.html', title='Signup')

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
   if request.method == 'POST':
       name = request.form.get('name')
       email = request.form.get('email')
       pass_encrypted = Fernet(key_2.encode()).encrypt(request.form.get('pass').encode())
       
       return f"name: {name}, email: {email}, ep: {pass_encrypted.decode()}"
   else:
       return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=1234)