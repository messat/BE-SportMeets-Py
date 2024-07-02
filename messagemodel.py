import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify
def SelectAllMessagesByEventID(event_id): 
    """Selects all messages from the messages table that have a certain event ID in the PostgreSQL database"""
    try:
        with psycopg2.connect("dbname=sport_meets_test") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM messages WHERE event_id = %s;
                """
                cur.execute(command, (event_id,))
                messages = cur.fetchall()
                return jsonify({"messages": messages})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")