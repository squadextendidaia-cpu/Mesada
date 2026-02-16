# requirements.txt
Flask
Flask-RESTful
Flask-Mysqldb

# main.py
from flask import Flask
from flask_restful import Api, Resource
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return 'API is running!'

if __name__ == '__main__':
    app.run(debug=True)