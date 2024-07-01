import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS users
        """,
        """
        DROP TABLE IF EXISTS events
        """,
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            password VARCHAR(100) NOT NULL,
            avatar_url VARCHAR NOT NULL)
        """,
        """
        CREATE TABLE events (
            event_id SERIAL PRIMARY KEY,
            event_name VARCHAR(150) NOT NULL,
            event_img_url VARCHAR(150) NOT NULL,
            event_description VARCHAR(150) NOT NULL,
            event_location VARCHAR(150) NOT NULL,
            event_date DATE NOT NULL,
            event_spaces_available VARCHAR(150) NOT NULL
            )
        """,
    )
    try:
      
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()