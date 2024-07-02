import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify

def SelectAllEvents():
    """Selects all events from events table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM events;
                """
                cur.execute(command)
                events = cur.fetchall()
                return jsonify({"events": events})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")

def SelectEventByID(event_id): 
    """Selects an individual user from users table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM events WHERE event_id = %s;
                """
                cur.execute(command, (event_id,))
                event = cur.fetchall()
                return jsonify({"event": event})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")

def AddEvent(newEvent): 
    """Post a new Event to the events table in the PostgreSQL database"""
    print(newEvent["event_name"])
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                    INSERT INTO events (event_name, event_img_url, event_description, event_location, created_at, event_spaces_available, event_category, event_organiser)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
                    """
                cur.execute(command, (newEvent["event_name"], newEvent["event_img_url"], newEvent["event_description"], newEvent["event_location"], newEvent["created_at"],  newEvent["event_spaces_available"],newEvent["event_category"],newEvent["event_organiser"]))
                addedevent = cur.fetchone()  # Use fetchone() for single row return
                return jsonify({"PostedEvent": addedevent})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")