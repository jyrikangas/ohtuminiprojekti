import unittest
from references_repository import get_references
from StubDBConn import StubDBConn

class TestReferencesRepository(unittest.TestCase):


    def test_get_references_returns_correct_list(self):
        references = get_references(StubDBConn())
        self.assertTrue(len(references)>0)