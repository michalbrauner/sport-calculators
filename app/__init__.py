from flask import Flask
from flask import render_template
from flask import Request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('general/index.html')


@app.route("/calculate-run", methods=["POST"])
def calculate_run():

    response_data = {"result": False}

    if Request.method == "POST":
        response_data.result = True

    return jsonify(response_data)


@app.errorhandler(404)
def not_found(error):
    return "Page not found"
