from flask import Flask, render_template

app = Flask(__name__)


# FLASK_APP=app.py flask run
# FLASK_APP=app.py FLASK_ENV=development flask run


@app.route("/")
def hello_world():
    name = "Yemi"
    return render_template("index.html", name=name)


@app.route("/french")
def bonjour_french():
    return "Bonjour World!"


@app.route("/name/<name>")
def hello_name(name):
    return f"Hello {name}"
