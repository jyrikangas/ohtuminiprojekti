# pylint: skip-file
import unittest
from references_repository import get_references, add_book, delete_book, get_reference_by_id, generate_bibtex
from database import get_db_connection

class TestReferencesRepository(unittest.TestCase):
    def setUp(self):
        self.data = [('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall', 'computer science')]
        self.conn = get_db_connection(test=True)

        # Create a test db
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS book")
        cur.execute(
            "CREATE TABLE book (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT, addedDate timestamp, tag TEXT)"
            )
        cur.execute(
            "INSERT INTO book (author, title, year, publisher, tag) VALUES ('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall', 'computer science')"
            )
        self.conn.commit()


    def test_get_references_returns_correct_list(self):
        references = get_references(self.conn)
        self.assertTrue(len(references) == 1)

    def test_get_reference_by_id(self):
        reference = get_reference_by_id('1', self.conn)
        self.assertEqual(reference[0][1], self.data[0][0])

    def test_get_reference_by_id_with_wrong_id(self):
        reference = get_reference_by_id('aa', self.conn)
        self.assertEqual(reference, [])

    def test_add_book_with_correct_input(self):
        add_book('TestEst', 'TEsting is fun', 2000,
                 'Tester publishing', 'test', self.conn)
        references = get_references(self.conn)
        self.assertTrue(len(references) == 2)

    def test_add_book_with_wrong_length(self):
        added = add_book('', 'TEsting is fun', 2000,
                         'Tester publishing', 'test', self.conn)

        self.assertEqual(added, 'Syötteen pituus on oltava yli 1')

    def test_add_book_with_wrong_types(self):
        added = add_book(1000, 'TEsting is fun', 2000,
                         'Tester publishing', 'test', self.conn)

        self.assertEqual(added, 'Kirjailijan on oltava merkkijono')

        added = add_book('test', 1222, 2000,
                         'Tester publishing', 'test', self.conn)

        self.assertEqual(added, 'Otsikon on oltava merkkijono')

        added = add_book('test', 'test test', '2000',
                         'Tester publishing', 'test', self.conn)

        self.assertEqual(added, 'Vuoden on oltava numero')

        added = add_book('test', 'test test', 2000,
                         1222, 'test', self.conn)

        self.assertEqual(added, 'Julkaisijan on oltava merkkijono')


    def test_delete_book(self):
        delete_book('1', self.conn)
        references = get_references(self.conn)
        self.assertTrue(len(references) == 0)

    def test_delete_book_with_wrong_id(self):
        deleted = delete_book('aa', self.conn)
        self.assertEqual(deleted, 'Kirjan poistamisessa tapahtui virhe')

    def test_generate_bibtex(self):
        viite = get_reference_by_id('1', self.conn)
        bibtex = generate_bibtex(viite)
        correct_bibtex = """@book{viite,\n author = {Martin, Robert},\n publisher = {Prentice Hall},\n title = {Clean Code: A Handbook of Agile Software Craftsmanship},\n year = {2008}\n}\n"""
        print(bibtex)
        print(correct_bibtex)
        self.assertEqual(bibtex, correct_bibtex)