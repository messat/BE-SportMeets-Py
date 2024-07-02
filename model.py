from psycopg2.extras import RealDictCursor
import psycopg2

def selectAllUsers():
    """Selects all users from users table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM users;
                """
                cur.execute(command)
                users = cur.fetchall()
                return users
        print('Successfully selected user data from the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")