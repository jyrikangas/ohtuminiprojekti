# pylint: skip-file
from database import the_db_connection

def init_db():
    conn = the_db_connection
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS book")
    cur.execute("CREATE TABLE book (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT)")
    cur.execute(
        "INSERT INTO book (author, title, year, publisher) VALUES ('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall')"
        )
    cur.execute(
        "INSERT INTO book (author, title, year, publisher) VALUES ('Tolkien, John', 'The Lord of the Rings', 1954, 'Allen & Unwin')"
        )
    conn.commit()

if __name__ == '__main__':
    init_db()
