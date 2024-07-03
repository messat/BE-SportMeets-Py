import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify

def SelectAllEvents(location, event_category):
    """Selects all events from events table in the PostgreSQL database"""
    if isinstance(location, str) and isinstance(event_category, str):  # Correct type check
        try:
            with psycopg2.connect("dbname=sport_meets_test") as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    command = """
                    SELECT * FROM events WHERE event_location = %s and event_category = %s;
                    """
                    cur.execute(command, (location, event_category,))
                    events = cur.fetchall()
                    return jsonify({"events": events})
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error: {error}")

    if isinstance(location, str):
          # Correct type check
        try:
            with psycopg2.connect("dbname=sport_meets_test") as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    command = """
                    SELECT * FROM events WHERE event_location = %s;
                    """
                    cur.execute(command, (location,))
                    events = cur.fetchall()
                    return jsonify({"events": events})
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error: {error}")

    if isinstance(event_category, str):  # Correct type check
        try:
            with psycopg2.connect("dbname=sport_meets_test") as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    command = """
                    SELECT * FROM events WHERE event_category = %s;
                    """
                    cur.execute(command, (event_category,))
                    events = cur.fetchall()
                    return jsonify({"events": events})
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error: {error}")
    
    else:
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


def updatingASingleEvent(updatedEvent, event_id): 
    """Updating a single event in the events table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                update_command = """
                    UPDATE events 
                    SET event_name = %s, event_img_url = %s, event_description = %s, event_location = %s, event_spaces_available = %s, event_category = %s, event_organiser = %s
                    WHERE event_id = %s
                    RETURNING *;
                    """
                cur.execute(update_command, (
                    updatedEvent["event_name"], 
                    updatedEvent["event_img_url"], 
                    updatedEvent["event_description"], 
                    updatedEvent["event_location"], 
                    updatedEvent["event_spaces_available"],
                    updatedEvent["event_category"],
                    updatedEvent["event_organiser"],
                    event_id
                ))
                updatedAnEvent = cur.fetchone()  # Use fetchone() for single row return
                return jsonify({"UpdatedEvent": updatedAnEvent})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return jsonify({"error": str(error)})
    


def deleteById(event_id): 
    """Deletes a single event in the events table in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                delete_command = """
                    DELETE from events 
                    WHERE event_id = %s
                    """
                cur.execute(delete_command, (event_id))
                deleteEvent = cur.fetchone()  # Use fetchone() for single row return
                return "Succesfully Deleted"
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        return jsonify({"error": str(error)})
    