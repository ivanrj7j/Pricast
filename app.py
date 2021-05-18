from flask import *
from flask_sqlalchemy import *
# importing the libraries and packages needed 
app = Flask(__name__)

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
       pass
   else:
       return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=1234)