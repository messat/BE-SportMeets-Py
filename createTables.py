import psycopg2
from index import load_config

import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            password VARCHAR(100) NOT NULL,
            avatar_url VARCHAR NOT NULL
        )
        """)
    try:
        config = load_config()
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

