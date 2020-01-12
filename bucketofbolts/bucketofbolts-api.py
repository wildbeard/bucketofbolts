from flask import Flask, request, jsonify
import sqlalchemy
import os
import logging

from models.User import User
from models.Bolt import Bolt

app = Flask(__name__)

# DB Stuff
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')

connString = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_DATABASE}'
db = sqlalchemy.create_engine(connString, echo=True)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=db)
session = Session()

@app.before_request
def auth():
    json = request.json
    if json is not None:
        token = json.get('token')
    else:
        token = request.headers.get('X-BoB-Token')
    
    app.logger.info(token)

    if token is False or token is None:
        return jsonify({
            'status': 200,
            'message': 'Token must be provided'
        })
    elif token != '123':
        return jsonify({
            'status': 200,
            'message': 'Unauthorized'
        })

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/users')
def listUsers():
    users = session.query(User).all()
    return jsonify({
        'status': 200,
        'data': users
    })

@app.route('/bolts')
def listBolts():
    bolts = session.query(Bolt).filter(Bolt.hardware_type).all()
    return jsonify({
        'status': 200,
        'data': bolts
    })