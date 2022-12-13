from flask import Flask, render_template, request, redirect, Response
from references_repository import get_references, add_book, delete_book, get_reference_by_id
from references_repository import get_unique_tags, get_references_by_tag_and_sort
from references_repository import generate_bibtex
from database import the_db_connection
from init_db import check_db

app = Flask(__name__, template_folder='templates')
check_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/viitteet/download")
def download_bibtex():
    viite_id = request.args.get("id")
    references = get_reference_by_id(viite_id, the_db_connection)
    print(references)
    if viite_id is None:
        references = get_references(the_db_connection)

    bibtex = generate_bibtex(references)
    return Response(
        bibtex,
        mimetype="text/plain",
        headers={"Content-disposition":
                 "attachment; filename=references.bib"})


@app.route("/viitteet/")
def list_references():
    tag = request.args.get('tag')
    if tag is None:
        tag = "all"
    error = request.args.get('error')
    sort = request.args.get('sort')
    references = get_references_by_tag_and_sort(tag, sort, the_db_connection)
    tags = get_unique_tags(the_db_connection)
    bibtex = generate_bibtex(references)
    return render_template("viitteet.html", viitteet=zip(references, bibtex), tags=tags, error=error, sorts=["year_asc", "year_desc", "added_asc", "added_desc"])


@app.route("/lisaa_viite", methods=["GET", "POST"])
def add_viite():
    if request.method == "POST":
        author = request.form["author"]
        title = request.form["title"]
        year = int(request.form["year"])
        publisher = request.form["publisher"]
        tag = request.form["tag"]

        refname = request.form["refname"]
        added_book = add_book(author, title, year, publisher, tag, refname, the_db_connection)
        if added_book is not True:
            return render_template("lisaa_viite.html", error=added_book)

        return redirect("/viitteet/?error=" + "Viite lisätty onnistuneesti")

    return render_template("lisaa_viite.html")


@app.route("/poista_viite")
def delete_viite():
    viite = request.args.get("id")
    deleted = delete_book(viite, the_db_connection)
    if deleted is not True:

        return redirect("/viitteet/?error=" + deleted)

    return redirect("/viitteet/?error=" + "Viite poistettu onnistuneesti")

if __name__ == "__main__":
    app.run(debug=True)
