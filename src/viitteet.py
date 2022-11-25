from database import get_db_connection

database_connection = get_db_connection()

##palauttaa kaikki viitteet jossain muodossa
def hae_viitteet():
    cursor = database_connection.cursor()
    viitteet = cursor.execute("SELECT * FROM book; ")
    return viitteet

##tänne metodi jolla voi lisätä viitteitä