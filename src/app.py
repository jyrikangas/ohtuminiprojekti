from flask import Flask, render_template, request
from references_repository import get_references, add_book

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viitteet")
def list_references():
    references = get_references()
    print(references)
    return render_template("viitteet.html", viitteet=references)


@app.route("/lisaa_viite", methods=["GET", "POST"])
def add_viite():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        add_book(author, title, year, publisher)
        return render_template("index.html")

    return render_template("lisaa_viite.html")
