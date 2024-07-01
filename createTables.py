import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            username VARCHAR(200) PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            password VARCHAR(200) NOT NULL,
            avatar_url VARCHAR(1000) NOT NULL
        )
        """)
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                    cur.execute(commands)
                    print('Successfully Created tables')
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)



