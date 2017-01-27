from flask import Flask
from flask import render_template
from flask import jsonify
from calculator_run.form import CalculatorForm as RunCalculatorForm
from calculator_run.calculator import Calculator as RunCalculator
import app.convertors

app = Flask(__name__)


@app.route("/")
def index():
    form_run = RunCalculatorForm()
    return render_template('general/index.html', form_run=form_run)


@app.route("/calculate-run", methods=["POST"])
def calculate_run():

    response_data = {"result": False, "errors": {}, "result_data": {}}

    form = RunCalculatorForm()

    if form.validate_on_submit():
        response_data["result"] = True
        calculator = RunCalculator(form)

        result_value = calculator.calculate()
        result_type = calculator.get_field_to_calculate()

        if result_type == 'distance':
            response_data["result_data"] = dict(distance=result_value)

        elif result_type == 'tempo':
            response_data["result_data"] = dict(tempo=convertors.convert_seconds_to_tempo(result_value))

        elif result_type == 'time':
            response_data["result_data"] = dict(time=convertors.convert_seconds_to_time(result_value))

    else:
        response_data["errors"] = form.errors

    return jsonify(response_data)


@app.errorhandler(404)
def not_found(error):
    return "Page not found"
