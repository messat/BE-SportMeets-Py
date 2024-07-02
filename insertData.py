import psycopg2
import json

def insert_User_Data():
    """Inserts user data into tables in the PostgreSQL database"""
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

            print('Successfully inserted user data into the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"First Error: {error}")
    finally:
        if conn:
            conn.close()



def insert_Event_Data():
    """Inserts events data into tables in the PostgreSQL database"""
    with open('./data/eventData.json') as file_object:
        event_data = json.load(file_object)
    try:
        with psycopg2.connect(dbname="sport_meets_test") as conn:
            with conn.cursor() as cur:
                for event in event_data:
                    command = """
                    INSERT INTO events (event_name, event_img_url, event_description, event_location, created_at, event_spaces_available, event_category, event_organiser)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
                    """
                    values = (event["event_name"], event["event_img_url"], event["event_description"], event["event_location"], event["created_at"], event["event_spaces_available"], event["event_category"], event["event_organiser"])
                    cur.execute(command, values)
                    conn.commit()
                    
                print('Successfully inserted event data into the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Second Error: {error}")
    finally:
        if conn:
            conn.close()

def insert_Junction_Data():
    """Inserts junctions data into tables in the PostgreSQL database"""
    with open('./data/junction.json') as file_object:
        junction_data = json.load(file_object)
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor() as cur:
                for junc in junction_data:
                    command = """
                    INSERT INTO user_events_junction (username, event_id)
                    VALUES (%s, %s) RETURNING *;
                    """
                    values = (junc["username"], junc["event_id"])
                    cur.execute(command, values)
                    conn.commit()
                    
                print('Successfully inserted junction data into the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Second Error: {error}")
    finally:
        if conn:
            conn.close()


def insert_Messages_Data():
    """Inserts Messages data into tables in the PostgreSQL database"""
    with open('./data/messagesData.json') as file_object:
        messages_data = json.load(file_object)
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor() as cur:
                for message in messages_data:
                    command = """
                    INSERT INTO messages (message_body, sender, event_id)
                    VALUES (%s, %s, %s) RETURNING *;
                    """
                    values = (message["message_body"], message["sender"], message["event_id"])
                    cur.execute(command, values)
                    conn.commit()
                    
                print('Successfully inserted messages data into the table')
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Second Error: {error}")
    finally:
        if conn:
            conn.close()
