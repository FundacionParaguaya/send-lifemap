import os
from flask import Flask, request, jsonify, render_template, send_file, Response, url_for, json
from connect_database import connect_mongo, get_lifemap, save_number
from twilio_helpers import send_template, send_messages, send_pdf
import pdfkit

BASE_URL = os.getenv("BASE_URL")
PDF_DIR="./static/pdf/"
app = Flask(__name__)


@app.route("/")
def hello_world():
    db = connect_mongo()
    family = db["family"]
    # exclude _id Mongo's ObjectID field for correct jsonification
    query = list(family.find({}, {"_id": 0}))
    return jsonify(query)

@app.route("/message-form")
def message_form():
    return render_template("message-form.html")

@app.route("/send-initial-message", methods=["POST"])
def send_inital_message():
    from_number = request.form["From"]
    return jsonify(send_template(from_number))

@app.route("/send-reminders", methods=["POST"])
def send_reminder():
    indicator = request.form['indicator']
    message = request.form['message']
    print(indicator, message)
    send_messages(indicator, message)
    return render_template("message-success.html")

@app.route("/send-lifemap", methods=["POST"])
def send_lifemap():
    phone_number = request.form['From']
    save_number(phone_number)
    pdfnetor(phone_number)
    lifemap = send_pdf(phone_number)
    return jsonify("pdf successfully sent")

@app.route("/render-template", methods=["GET", "POST"])
def render_graphic():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "snapshot_sample.json")
    data = json.load(open(json_url))
    return render_template('template-lifemap.html', dato=data)

@app.route("/render-template/<string:number>", methods=["GET", "POST"])
def number_graphic(number):
    FALLBACK_NUMBER = '+595 000 000 000'
    print(number)
    values = {}
    db = connect_mongo()
    data = db.family.find_one({"phoneNumber":number})
    if not data: 
        data = db.family.find_one({"phoneNumber":FALLBACK_NUMBER})
    # if lifemap:
        # for v in range(1,4):
        #     key = float(v)
        #     values[key]=sum(value == key for value in lifemap.values())
    return render_template('template-lifemap.html', dato=data)

    # return render_template("chart_values.html", semaforo=values, lifemap=lifemap)

@app.route("/generate-pdf/<string:number>")
def pdfnetor(number):
    pdf = pdfkit.from_url(
        f"{BASE_URL}render-template/{number}",
        f"{PDF_DIR}{number}.pdf",
        options={"javascript-delay":2000})
    print(pdf,"!!!!!!!!!!!!")
    return send_file(f"{PDF_DIR}{number}.pdf")
    #return jsonify(pdf)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
