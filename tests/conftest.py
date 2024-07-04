# conftest.py
import pytest
import psycopg2
from createTables import create_tables
from insertData import insert_User_Data, insert_Event_Data, insert_Junction_Data, insert_Messages_Data

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        conn = psycopg2.connect("dbname=sport_meets_test")
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        raise

@pytest.fixture(scope='function', autouse=True)
def setup_database():
    """ Set up and seed the database before each test """
    conn = connect()
    with conn.cursor() as cur:
        create_tables(conn)
        insert_User_Data(conn)
        insert_Event_Data(conn)
        insert_Junction_Data(conn)
        insert_Messages_Data(conn)
    conn.commit()
    yield conn
    conn.close()
