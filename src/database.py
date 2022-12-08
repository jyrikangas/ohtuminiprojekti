import sqlite3

DATABASE = 'database.db'
TEST_DATABASE = 'database_test.db'

def get_db_connection(test=False):
    db_path = DATABASE if not test else TEST_DATABASE
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn

the_database_connection = get_db_connection()
