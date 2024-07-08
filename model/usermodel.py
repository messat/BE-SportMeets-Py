from psycopg2.extras import RealDictCursor
import psycopg2
from flask import jsonify

production = "user=postgres.agqagyjrdydvkyawzzwc password=Wwdc13xcode! host=aws-0-eu-west-2.pooler.supabase.com port=6543 dbname=postgres"
development = "dbname=sport_meets_test"
enviroment = "development"

def selectAllUsers():
    """Selects all users from users table in the PostgreSQL database"""
    try:
        if (enviroment == "production"):
            with psycopg2.connect("user=postgres.agqagyjrdydvkyawzzwc password=Wwdc13xcode! host=aws-0-eu-west-2.pooler.supabase.com port=6543 dbname=postgres") as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                  command = """ 
                   SELECT * FROM users;
                """
                cur.execute(command)
                users = cur.fetchall()
                return jsonify({"users": users})
        elif (enviroment == "development"):
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
        with psycopg2.connect(enviroment) as conn:
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


def addSingleUser(newUserData): 
    print("Model", newUserData)
    """Add a new user to users table in the PostgreSQL database"""
    try:
        with psycopg2.connect(enviroment) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                INSERT INTO users (username, name, password, avatar_url)
                VALUES (%s, %s, %s, %s) RETURNING *;                
                """
                cur.execute(command, (newUserData["username"], newUserData["name"], newUserData["password"], newUserData["avatar_url"]))
                user = cur.fetchone()
                return jsonify({"newUser": user})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")


def updateSingleUser(updatedUser, username): 
    """Updating a single user in the events table in the PostgreSQL database"""
    try:
        with psycopg2.connect(enviroment) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                update_command = """
                    UPDATE users 
                    SET name = %s, password = %s, avatar_url = %s
                    WHERE username = %s
                    RETURNING *;
                    """
                cur.execute(update_command, (
                    updatedUser["name"], 
                    updatedUser["password"], 
                    updatedUser["avatar_url"], 
                    username
                ))
                updatedSingleUser = cur.fetchone()  # Use fetchone() for single row return
                return jsonify({"UpdatedUser": updatedSingleUser})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return jsonify({"error": str(error)})
    