from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viitteet")
def viitteet():
    ##viitteet = db.findAll()
    return render_template("viitteet.html", viitteet=viitteet)