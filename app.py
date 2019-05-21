from flask import Flask, request, jsonify, render_template, send_file
from connect_database import connect_mongo
# from twilio_helpers import send_template, send_messages
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

@app.route('/send-lifemap', methods = ['GET'])
def send_lifemap():
    # template = render_template('lifemap.html', json_data=data)
    # template = template.encode('utf-8')
    pdf = pdfkit.from_url('127.0.0.1:5000/render-template', 'output.pdf')
    return jsonify("success")

    # deliver_via_whatsapp(lifemap)
@app.route('/render-template', methods=["GET"])
def display_graphic():
    return render_template('grafic.html')

# template = get_template("output_pdf.html")
# context = Context({"data": data})  # data is the context data that is sent to the html file to render the output. 
# html = template.render(context)  # Renders the template with the context data.
# pdfkit.from_string(html, 'out.pdf')
# pdf = open("out.pdf")
# response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
# response['Content-Disposition'] = 'attachment; filename=output.pdf'
# pdf.close()
# os.remove("out.pdf")  # remove the locally created pdf file.
# return response  # returns the response.