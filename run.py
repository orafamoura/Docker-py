from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return 'Ola, estou na aplicacao setada'
