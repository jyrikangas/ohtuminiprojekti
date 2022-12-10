from flask import Flask, render_template, request, redirect
from references_repository import get_references, add_book, delete_book, get_tags
from database import the_db_connection
from init_db import check_db

app = Flask(__name__, template_folder='templates')
check_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/viitteet")
def list_references():

    references = get_references(the_db_connection)
    all_tags = get_tags(the_db_connection)
    tags = []
    for tag in all_tags:
        if tag not in tags:
            tags.append(tag)
    print(tags)
    return render_template("viitteet.html", viitteet=references, tags=tags)


@app.route("/lisaa_viite", methods=["GET", "POST"])
def add_viite():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        year = int(request.form["year"])
        publisher = request.form["publisher"]
        tag = request.form["tag"]
        added_book = add_book(author, title, year, publisher, tag, the_db_connection)
        print(added_book)
        if added_book is not True:
            return render_template("lisaa_viite.html", error=added_book)
        return redirect("/viitteet")

    return render_template("lisaa_viite.html")

@app.route("/poista_viite")
def delete_viite():
    viite = request.args.get("viite_id")
    delete_book(viite, the_db_connection)
    return redirect("/viitteet")

@app.route("/sort_by_year")
def sort_by_year():
    references = get_references(the_db_connection)
    sorted_references = sorted(references, key = lambda viite: viite[3])
    return render_template("viitteet.html", viitteet=sorted_references)
