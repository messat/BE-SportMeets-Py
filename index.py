import psycopg2
from createTables import create_tables
from insertData import insert_User_Data 
from insertData import insert_Event_Data
from insertData import insert_Junction_Data
from insertData import insert_Messages_Data

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    conn = connect()
    create_tables()
    insert_User_Data()
    insert_Event_Data()
    insert_Junction_Data()
    insert_Messages_Data()