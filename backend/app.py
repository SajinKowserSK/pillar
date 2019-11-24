from flask import Flask, request, jsonify
from dbHelper import PatientDBHelper, DoctorNotesHelper, DispenseDBHelper
from summarizer import summarize
from face_rekog import face_eval
from flask import render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

CURRENT_STATE = ""
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
        dnh = DoctorNotesHelper()
        data = dnh.getNote(pin)
        print(data)
        res = {'message': data['notes'][-1]['message']}
        return jsonify(res)

@app.route('/sendNote/',methods=['POST'])
def sendNote():
    print("GOt here.")
    pin = request.form['userPin']
    note = request.form['doctorNote']
    print(pin, note)
    d = DoctorNotesHelper()
    d.addNoteForPatient(pin, note)

    return "Hi"

@app.route('/sPatient/', methods=['GET'])
def getPatientDataFor():
    p = PatientDBHelper()
    name = request.args.get("name")
    return p.getDataForPatientName(name)

@app.route('/patients/', methods=['GET'])
def patientData():
    p = PatientDBHelper()
    return jsonify(p.getAllPatients())


@app.route('/dispense/', methods=['POST'])
def dispensePing():
    pin = request.args.get('pin')
    pdb = PatientDBHelper()
    data = pdb.getDataForPatient(str(pin))
    dis = DispenseDBHelper()
    dis.toggleDispense()
    msg = "Your prescription is "
    for prescription in data['prescription']:
        msg += prescription['dosage'] + \
            ' of ' + prescription['name'] + \
            ' ' + prescription['instruction']
    msg += ' You will get a text for your next pickup!'
    res = {'num_prescriptions': len(data['prescription']), 'message': msg}
    return jsonify(res)

@app.route('/setState/', methods=['POST'])
def setState():
    print(request.form['personName'])

    return "Hello"




if __name__ == "__main__":
    app.run(debug=False)
