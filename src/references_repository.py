from database import get_db_connection

database_connection = get_db_connection()

##palauttaa kaikki viitteet jossain muodossa
def get_references():
    cursor = database_connection.cursor()
    references = cursor.execute("SELECT * FROM book;")
    return references

##tänne metodi jolla voi lisätä viitteitä