from flask import Flask, render_template, request, redirect
from references_repository import get_references, add_book, delete_book
from database import get_db_connection

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viitteet")
def list_references():

    references = get_references(get_db_connection())
    return render_template("viitteet.html", viitteet=references)


@app.route("/lisaa_viite", methods=["GET", "POST"])
def add_viite():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        year = int(request.form["year"])
        publisher = request.form["publisher"]
        added_book = add_book(author, title, year, publisher, get_db_connection())
        print(added_book)
        if added_book is not True:
            return render_template("lisaa_viite.html", error=added_book)
        return redirect("/viitteet")

    return render_template("lisaa_viite.html")

@app.route("/poista_viite")
def delete_viite():
    viite = request.args.get("viite_id")
    delete_book(viite, get_db_connection())
    return redirect("/viitteet")
