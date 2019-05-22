from flask import Flask, request, jsonify, render_template
from connect_database import connect_mongo, get_lifemap
from twilio_helpers import send_template, send_messages
import pdfkit

app = Flask(__name__)

@app.route('/')
def hello_world():
    db = connect_mongo()
    family = db['family']
    return str(list(family.find()))

    # return str(list(family.find()))

@app.route('/send-initial-message', methods = ['POST'])
def send_inital_message():
    from_number = request.form['from']
    return jsonify(send_template(from_number))

@app.route('/send-reminders', methods = ['POST'])
def send_reminder():
    return jsonify(send_messages())

@app.route('/send-lifemap', methods=['GET','POST'])
def send_lifemap():
    phone_number = '+595000000'
    lifemap = get_lifemap(phone_number)
    return lifemap

@app.route('/render-template', methods=['GET','POST'])
def render_graphic():
    return render_template("grafic.html")
