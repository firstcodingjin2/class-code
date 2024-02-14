from flask import Flask
from flask import request
import sqlalchemy


print('check', sqlalchemy.__version__)

app = Flask('myWeb');

@app.route('/')
def index():
    return '<h1>test app</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'pass'

@app.route('/submit', methods=['GET'])
def submit():
    return 'pass123'

app.debug = True
app.run()

