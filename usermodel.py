from psycopg2.extras import RealDictCursor
import psycopg2
from flask import jsonify

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
                return jsonify({"users": users})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
            
def selectByUsername(username): 
    """Selects an individual user from users table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM users WHERE username = %s;
                """
                cur.execute(command, (username,))
                user = cur.fetchall()
                print('Successfully selected user data from the table')
                return jsonify({"user": user})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
