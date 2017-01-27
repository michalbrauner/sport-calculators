from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from calculator_run.form import CalculatorForm as RunCalculatorForm

app = Flask(__name__)


@app.route("/")
def index():
    form_run = RunCalculatorForm(csrf_enabled=False)
    return render_template('general/index.html', form_run=form_run)


@app.route("/calculate-run", methods=["POST"])
def calculate_run():

    response_data = {"result": False, "errors": {}}

    form = RunCalculatorForm(csrf_enabled=False)

    if form.validate_on_submit():
        response_data["result"] = True
    else:
        response_data["errors"] = form.errors

    return jsonify(response_data)


@app.errorhandler(404)
def not_found(error):
    return "Page not found"
