from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = "postgresql://backup_user:1234@192.168.214.100:5000/nohup"

db = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name}!</h1>'