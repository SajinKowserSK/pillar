from flask import Flask, request

from summarizer import summarize

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route('/summarize/', methods=['GET', 'POST'])
def summarizer():
    if request.method == 'POST':
        data = request.form
        return (summarize(data["text"]))


if __name__ == "__main__":
    app.run(debug=False)
