import sqlite3

DATABASE = 'database.db'
TEST_DATABASE = 'database_test.db'

def get_db_connection(test=False):
    conn = sqlite3.connect(DATABASE if not test else TEST_DATABASE)
    return conn

the_database_connection = get_db_connection()
