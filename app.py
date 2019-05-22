from flask import Flask, request, jsonify, render_template
from connect_database import connect_mongo
from twilio_helpers import send_template, send_messages
import pdfkit

app = Flask(__name__)

@app.route('/')
def hello_world():
    # db = connect_mongo()
    # family = db['family']

    # lifemap_data = json.dumps(list(family.find()))
    # send_lifemap(lifemap_data)
    send_lifemap('data/snapshot_sample.json')
    return render_template('grafic.html')

    # return str(list(family.find()))

@app.route('/send-initial-message', methods = ['POST'])
def send_inital_message():
    from_number = request.form['from']

    return jsonify(send_template(from_number))

@app.route('/send-reminders', methods = ['POST'])
def send_reminder():
    return jsonify(send_messages())

@app.route('/send-lifemap', methods = ['POST'])
def send_lifemap(data):
    # template = render_template('lifemap.html', json_data=data)
    # template = template.encode('utf-8')
    return pdfkit.from_file('templates/grafic.html', "lifemap.pdf")

    # deliver_via_whatsapp(lifemap)
