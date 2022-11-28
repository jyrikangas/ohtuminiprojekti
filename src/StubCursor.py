
class Cursor:
    
    def __init__(self):
        self.data = [('Martin, Robert', 'Clean Code: A Handbook of Agile Software Craftsmanship', 2008, 'Prentice Hall')]

    def execute(self, command):
        print(command)
        
    def fetchall(self):
        return self.data