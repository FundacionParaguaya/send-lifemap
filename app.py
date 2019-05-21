from flask import Flask
from connect_database import connect_mongo
app = Flask(__name__)

@app.route('/')
def hello_world():
    db = connect_mongo()
    family = db['family']

    return str(list(family.find()))