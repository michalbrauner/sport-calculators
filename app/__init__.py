from flask import Flask
from flask import render_template
from flask import jsonify
from calculator_run.form import CalculatorForm as RunCalculatorForm
from calculator_run.calculator import Calculator as RunCalculator
from calculator_swim.form import CalculatorForm as SwimCalculatorForm
from calculator_swim.calculator import Calculator as SwimCalculator
import app.convertors
import os

app = Flask(__name__)

if os.environ.get('IS_HEROKU', 0) == 0:
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.ProductionConfig')


@app.route("/")
def index():
    form_run = RunCalculatorForm()
    form_swim = SwimCalculatorForm()

    return render_template('general/index.html', form_run=form_run, form_swim=form_swim)


@app.route("/calculate-swim", methods=["POST"])
def calculate_swim():
    response_data = {"result": False, "errors": {}, "result_data": {}}

    form = SwimCalculatorForm()

    if form.validate_on_submit():
        response_data["result"] = True
        calculator = SwimCalculator(form)

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
