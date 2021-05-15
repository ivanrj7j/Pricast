from flask import *
from flask_sqlalchemy import *
# importing the libraries and packages needed 
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    app.run(debug=True, port=1234)