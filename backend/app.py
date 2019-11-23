from flask import Flask, request, jsonify
from dbHelper import PatientDBHelper
from summarizer import summarize
from face_rekog import face_eval
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
        name = request.args.get('name')
        pdb = PatientDBHelper()
        data = pdb.getDataForPatient(name)
        res = {'summary': data['medicalRecord'][0]['data']['summary']}
        return jsonify(res)


if __name__ == "__main__":
    app.run(debug=False)
