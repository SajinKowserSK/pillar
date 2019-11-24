from flask import Flask, request, jsonify
from dbHelper import PatientDBHelper
from summarizer import summarize
from face_rekog import face_eval
from flask import render_template
import sms
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route('/summarize/', methods=['GET', 'POST'])
def summarizer():
    if request.method == 'POST':
        data = request.form
        return summarize(data["text"])


@app.route('/face/', methods=['GET', 'POST'])
def face_match():
    if request.method == 'POST':
        data = request.form
        source, target = data['source'], data['target']
        return face_eval(source, target)


@app.route('/patient/', methods=['GET', 'POST'])
def patient():
    if request.method == 'GET':
        pin = request.args.get('pin')
        pdb = PatientDBHelper()
        data = pdb.getNote(pin)
        res = {'message': data['notes'][-1]['text']}
        return jsonify(res)


@app.route('/patients/', methods=['GET'])
def patientData():
    p = PatientDBHelper()
    print(p.getAllPatients())
    return jsonify(p.getAllPatients())


@app.route('/dispense/', methods=['GET'])
def dispensePing():
    pin = request.args.get('pin')
    pdb = PatientDBHelper()
    data = pdb.getDataForPatient(str(pin))
    msg = "Your prescription is "
    print(data['prescription'])
    for prescription in data['prescription']:
        msg += prescription['dosage'] + \
            ' of ' + prescription['name'] + \
            ' ' + prescription['instruction']
    msg += ' You will get a text for your next pickup!'
    res = {'num_prescriptions': len(data['prescription']), 'message': msg}
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=False)
