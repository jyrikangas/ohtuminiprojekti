from flask import Flask, render_template
from references_repository import get_references

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viitteet")
def list_references():
    references = get_references()
    print(references)
    return render_template("viitteet.html", viitteet=references)
