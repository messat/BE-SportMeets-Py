import psycopg2
import json

def insert_User_Data():
    """Inserts data into tables in the PostgreSQL database"""
    with open('./data/userData.json') as file_object:
        user_data = json.load(file_object)
    
    try:
        with psycopg2.connect(dbname="sport_meets_test") as conn:
            with conn.cursor() as cur:
                for user in user_data:
                    command = """
                    INSERT INTO users (username, name, password, avatar_url)
                    VALUES (%s, %s, %s, %s) RETURNING *;
                    """
                    values = (user["username"], user["name"], user["password"], user["avatar_url"])
                    cur.execute(command, values)
                    conn.commit()
                    print('Successfully inserted data into the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
    finally:
        if conn:
            conn.close()

