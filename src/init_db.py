# pylint: skip-file
from database import the_db_connection
import datetime

def empty_db():
    connection = the_db_connection
    cursor = connection.cursor()

    drop_table_query = """
        DROP TABLE IF EXISTS book
        """
    cursor.execute(drop_table_query)
    connection.commit()

def check_db():
    connection = the_db_connection
    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY, 
            author TEXT, 
            title TEXT, 
            year INTEGER, 
            publisher TEXT,
            date TIMESTAMP,
            tag TEXT,
            refname TEXT
        )
        """
    cursor.execute(create_table_query)
    connection.commit()

def insert_model_books_into_db():
    connection = the_db_connection
    cursor = connection.cursor()
    date = datetime.date.today()
    print(date)
    
    insert_query = """
        INSERT INTO book (
            author, title, year, publisher, date, tag, refname
        ) 
        VALUES (
            :author, :title, :year, :publisher, :date, :tag, :refname
        );
        """
    book1 = {"author": "Martin, Robert", "title":"Clean Code: A Handbook of Agile Software Craftsmanship", "year":2008, "publisher":"Prentice Hall", "date":date, "tag":"computer_science", "refname":"CleanCode"}
    book2 = {"author": "Tolkien, John", "title":"The Lord of the Rings", "year":1954, "publisher":"Allen & Unwin", "date":date, "tag":"fiction", "refname":"Lotr"}
    book3 = {"author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, Grady Booch", "title":"Design Patterns: Elements of Reusable Object-Oriented Software, 1st Edition", "year":1994, "publisher":"Addison-Wesley", "date":date, "tag":"computer_science", "refname":"DesignPatterns"}

    cursor.execute(insert_query, book1)
    cursor.execute(insert_query, book2)
    cursor.execute(insert_query, book3)
    connection.commit()

if __name__ == '__main__':
    empty_db()
    check_db()
    insert_model_books_into_db()