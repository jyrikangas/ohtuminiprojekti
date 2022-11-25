from database import get_db_connection


##palauttaa kaikki viitteet jossain muodossa
def get_references():
    database_connection = get_db_connection()
    cursor = database_connection.cursor()

    cursor.execute("SELECT * FROM book;")
    references = cursor.fetchall()
    return references

##tänne metodi jolla voi lisätä viitteitä