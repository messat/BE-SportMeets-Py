import psycopg2

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS messages
        """,
         """
        DROP TABLE IF EXISTS user_events_junction
        """,
        """
        DROP TABLE IF EXISTS events
        """,
        """
        DROP TABLE IF EXISTS users
        """,
        """
        CREATE TABLE users (
            username PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            password VARCHAR(100) NOT NULL,
            avatar_url VARCHAR NOT NULL
            )
        """,
        """
        CREATE TABLE events (
            event_id SERIAL PRIMARY KEY,
            event_name VARCHAR(150) NOT NULL,
            event_img_url VARCHAR(150) NOT NULL,
            event_description VARCHAR(150) NOT NULL,
            event_location VARCHAR(150) NOT NULL,
            created_at TIMESTAMP NOT NULL,
            event_spaces_available INT NOT NULL,
            event_organiser VARCHAR NOT NULL REFERENCES users(username)
            )
        """,
    """CREATE TABLE user_events_junction (
        username VARCHAR NOT NULL REFERENCES users(username),
        event_id INT NOT NULL REFERENCES events(event_id)
    )
    """,
    """CREATE TABLE messages (
        message_id SERIAL PRIMARY KEY, 
        message_body VARCHAR NOT NULL,
        created_at TIMESTAMP DEFAULT NOW(),
        sender VARCHAR(100) NOT NULL REFERENCES users(username),
        event_id INT NOT NULL REFERENCES events(event_id)
    )
    """
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