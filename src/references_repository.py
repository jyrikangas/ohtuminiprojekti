from database import get_db_connection


##palauttaa kaikki viitteet jossain muodossa
def get_references():
    database_connection = get_db_connection()
    cursor = database_connection.cursor()

    cursor.execute("SELECT * FROM book;")
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