from database import get_db_connection

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS book")
    cur.execute("CREATE TABLE book (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT)")
    cur.execute(
        "INSERT INTO book (author, title, year, publisher) VALUES ('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall')"
        )

if __name__ == '__main__':
    init_db()
