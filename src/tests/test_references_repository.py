import unittest
from references_repository import get_references, add_book
from database import get_db_connection

class TestReferencesRepository(unittest.TestCase):
    def setUp(self):
        self.data = [('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall')]
        self.conn = get_db_connection(test=True)

        # Create a test db
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS book")
        cur.execute(
            "CREATE TABLE book (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT)"
            )
        cur.execute(
            "INSERT INTO book (author, title, year, publisher) VALUES ('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall')"
            )
        self.conn.commit()

    

    def test_get_references_returns_correct_list(self):
        references = get_references(self.conn)
        self.assertTrue(len(references) == 1)

    def test_add_book(self):
        add_book('TestEst', 'TEsting is fun', 2000,
                 'Tester publishing', self.conn)
        references = get_references(self.conn)
        self.assertTrue(len(references) == 2)

    
