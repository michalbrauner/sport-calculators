from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is tempo calculator"


@app.errorhandler(404)
def not_found(error):
    return "Page not found"
