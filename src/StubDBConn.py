from StubCursor import Cursor

class StubDBConn:
    def __init__(self):
        pass
    def cursor(self):
        return Cursor()

