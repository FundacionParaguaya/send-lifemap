from flask import Flask, request, jsonify
from connect_database import connect_mongo
from twilio_helpers import send_template, send_messages
app = Flask(__name__)

@app.route('/')
def hello_world():
    db = connect_mongo()
    family = db['family']

    return str(list(family.find()))

@app.route('/send-initial-message', methods = ['POST'])
def send_inital_message():
    from_number = request.form['from']

    return jsonify(send_template(from_number))

@app.route('/send-reminders', methods = ['POST'])
def send_reminder():
    return jsonify(send_messages())
