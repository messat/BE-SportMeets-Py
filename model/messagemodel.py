import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify

def SelectAllMessagesByEventID(event_id): 
    """Selects all messages from the messages table that have a certain event ID in the PostgreSQL database"""
    try:
        with psycopg2.connect("user=postgres.agqagyjrdydvkyawzzwc password=Wwdc13xcode! host=aws-0-eu-west-2.pooler.supabase.com port=6543 dbname=postgres") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                SELECT * FROM messages WHERE event_id = %s ORDER BY created_at ASC;
                """
                cur.execute(command, (event_id,))
                messages = cur.fetchall()
                return jsonify({"messages": messages})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")

def AddNewMessage(newMessage):
    """Post a new message to the messages table in the PostgreSQL database"""
    try:
        with psycopg2.connect("user=postgres.agqagyjrdydvkyawzzwc password=Wwdc13xcode! host=aws-0-eu-west-2.pooler.supabase.com port=6543 dbname=postgres") as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                command = """
                    INSERT INTO messages (message_body, sender, event_id)
                    VALUES (%s, %s, %s) RETURNING *;
                    """
                cur.execute(command, (newMessage["message_body"], newMessage["sender"], newMessage["event_id"]))
                addedMessage = cur.fetchone()  # Use fetchone() for single row return
                return jsonify({"PostedMessage": addedMessage})
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")