from flask import Flask, request, jsonify
import sqlalchemy
import os

from models.User import User

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

users = session.query(User).filter_by(id=1).first()

@app.before_request
def auth():
    json = request.json
    if json is not None:
        token = json.get('token')
    else:
        token = request.headers.get('X-BoB-Token')
    
    if token is False or token is None:
        return jsonify({
            'status': 200,
            'user': users.to_dict(),
            'message': 'Token must be provided'
        })

@app.route('/')
def index():
    return 'Hello, World! Updated123'

@app.route('/', methods=[ 'POST' ])
def postIndex():
    message = 'Hello, %s' % request.json.get('Token')
    return jsonify({
        'status': 200,
        'message': message
    })
