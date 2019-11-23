from flask import Flask, request

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


if __name__ == "__main__":
    app.run(debug=False)
