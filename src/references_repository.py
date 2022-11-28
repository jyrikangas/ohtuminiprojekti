from database import get_db_connection


##palauttaa kaikki viitteet jossain muodossa
def get_references(db_conn):
    database_connection = db_conn
    cursor = database_connection.cursor()

    cursor.execute("SELECT (author, title, year, publisher) FROM book;")
    references = cursor.fetchall()
    return references


def add_book(author, title, year, publisher):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO book (author, title, year, publisher) VALUES (?, ?, ?, ?)',
        (author, title, year, publisher)
    )
    conn.commit()
    conn.close()
##tänne metodi jolla voi lisätä viitteitä