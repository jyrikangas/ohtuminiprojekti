##palauttaa kaikki viitteet jossain muodossa
def get_references(db_conn):
    database_connection = db_conn
    cursor = database_connection.cursor()

    cursor.execute("SELECT id, author, title, year, publisher FROM book;")
    references = cursor.fetchall()
    return references


def add_book(author, title, year, publisher, db_conn):


    if not isinstance(year, int):
        return "Vuoden on oltava numero"

    if not isinstance(author, str):
        return "Kirjailijan on oltava merkkijono"

    if not isinstance(title, str):
        return "Otsikon on oltava merkkijono"

    if not isinstance(publisher, str):
        return "Julkaisijan on oltava merkkijono"

    if len(author) < 1 or len(title) < 1 or year < 1 or len(publisher) < 1:
        return "Syötteen pituus on oltava yli 1"
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO book (author, title, year, publisher) VALUES (?, ?, ?, ?)',
        (author, title, year, publisher)
    )
    conn.commit()
    return True

def delete_book(viite, db_conn):
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute('DELETE FROM book WHERE id=?', viite)
    conn.commit()
