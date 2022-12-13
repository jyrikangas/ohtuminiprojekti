# pylint: skip-file
import datetime
import unittest
from references_repository import *
from database import get_db_connection

class TestReferencesRepository(unittest.TestCase):
    def setUp(self):
        self.data = [('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall', datetime.datetime.now(), 'computer_science', 'CleanCode')]
        self.conn = get_db_connection(test=True)

        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS book")
        cursor.execute(
            "CREATE TABLE book (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT, date timestamp, tag TEXT, refname TEXT)"
            )

        insert_query = """
            INSERT INTO book (
                author, title, year, publisher, tag, refname
            ) 
            VALUES (
                :author, :title, :year, :publisher, :tag, :refname
            );
            """
        book1 = {"author": "Martin, Robert", "title":"Clean Code: A Handbook of Agile Software Craftsmanship", "year":2008, "publisher":"Prentice Hall", "date":datetime.datetime.now(), "tag":"computer_science", "refname":"CleanCode"}
        book2 = {"author": "Tolkien, John", "title":"The Lord of the Rings", "year":1954, "publisher":"Allen & Unwin", "date":datetime.datetime.now(), "tag":"fiction", "refname":"Lotr"}
        book3 = {"author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, Grady Booch", "title":"Design Patterns: Elements of Reusable Object-Oriented Software, 1st Edition", "year":1994, "publisher":"Addison-Wesley", "date":datetime.datetime.now(), "tag":"computer_science", "refname":"DesignPatterns"}

        cursor.execute(insert_query, book1)
        cursor.execute(insert_query, book2)
        cursor.execute(insert_query, book3)
        self.conn.commit()

    def test_get_references_returns_correct_list(self):
        references = get_references(self.conn)
        self.assertTrue(len(references) == 3)

    def test_get_reference_by_id(self):
        reference = get_reference_by_id('1', self.conn)
        self.assertEqual(reference[0][1], self.data[0][0])

    def test_get_reference_by_id_with_wrong_id(self):
        reference = get_reference_by_id('aa', self.conn)
        self.assertEqual(reference, [])

    def test_add_book_with_correct_input(self):
        add_book('TestEst', 'TEsting is fun', 2000,
                 'Tester publishing', 'test', 'test', self.conn)
        references = get_references(self.conn)
        self.assertTrue(len(references) == 4)

    def test_add_book_with_wrong_length(self):
        added = add_book('', 'TEsting is fun', 2000,
                         'Tester publishing', 'test', 'test', self.conn)

        self.assertEqual(added, 'Syötteen pituus on oltava yli 1')

    def test_add_book_with_invalid_author(self):
        added = add_book(1000, 'TEsting is fun', 2000,
                         'Tester publishing', 'test', 'test', self.conn)

        self.assertEqual(added, 'Kirjailijan on oltava merkkijono')

    def test_add_book_with_invalid_name(self):
        added = add_book('test', 1222, 2000,
                         'Tester publishing', 'test', 'test', self.conn)

        self.assertEqual(added, 'Otsikon on oltava merkkijono')

    def test_add_book_with_invalid_year(self):
        added = add_book('test', 'test test', '2000',
                         'Tester publishing', 'test', 'test',self.conn)

        self.assertEqual(added, 'Vuoden on oltava numero')

    def test_add_book_with_invalid_publisher(self):
        added = add_book('test', 'test test', 2000,
                         1222, 'test', 'test',self.conn)

        self.assertEqual(added, 'Julkaisijan on oltava merkkijono')

    def test_delete_book(self):
        delete_book('1', self.conn)
        references = get_references(self.conn)
        self.assertTrue(len(references) == 2)

    def test_delete_book_with_wrong_id(self):
        deleted = delete_book('aa', self.conn)
        self.assertEqual(deleted, 'Kirjan poistamisessa tapahtui virhe')

    def test_get_correct_references_by_tag(self):
        tag = "computer_science"
        self.assertTrue(len(get_references_by_tag(tag, self.conn)) == 2)

        tag = "all"
        self.assertTrue(len(get_references_by_tag(tag, self.conn)) == 3)

    def test_get_correct_references_by_tag_and_sort_by_year_asc(self):
        tag = "computer_science"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_year_asc(tag, self.conn)[0][0], references[2][0])

        tag = "all"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_year_asc(tag, self.conn)[1][0], references[2][0])

    def test_get_correct_references_by_tag_and_sort_by_year_desc(self):
        tag = "computer_science"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_year_desc(tag, self.conn)[0][0], references[0][0])

        tag = "all"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_year_desc(tag, self.conn)[0][0], references[0][0])

    def test_get_correct_references_by_tag_and_sort_by_added_desc(self):
        tag = "computer_science"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_added_desc(tag, self.conn)[0][0], references[0][0])

        tag = "all"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort_by_added_desc(tag, self.conn)[0][0], references[0][0])

    def test_get_references_by_tag_and_sort_asc(self):
        tag = "computer_science"
        sort = "year_asc"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort(tag, sort, self.conn)[0][0],references[2][0])

    def test_get_references_by_tag_and_sort_desc(self):
        tag = "computer_science"
        sort = "year_desc"
        references = get_references(self.conn)
        self.assertEqual(get_references_by_tag_and_sort(tag, sort, self.conn)[0][0],references[0][0])

    def test_generate_bibtex(self):
        viite = get_reference_by_id('1', self.conn)
        bibtex = generate_bibtex(viite)

        correct_bibtex = """@book{CleanCode,\n author = {Martin, Robert},\n publisher = {Prentice Hall},\n title = {Clean Code: A Handbook of Agile Software Craftsmanship},\n year = {2008}\n}\n"""
        apulista = []
        apulista.append(correct_bibtex)
        self.assertEqual(bibtex, apulista)

    def test_get_tags(self):
        tags = get_tags(self.conn)
        print("test")
        print(tags)
        self.assertTrue(len(tags) == 3)
        self.assertEqual(tags[0][0], 'computer_science')

    def test_get_unique_tags(self):
        tags = get_unique_tags(self.conn)
        tags = list(filter(lambda x : x[0] != 'all', tags))
        self.assertTrue(len(tags) == 2)
        self.assertEqual(tags[0][0], 'computer_science')





    

