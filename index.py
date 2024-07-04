import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

from createTables import create_tables
from insertData import insert_User_Data, insert_Event_Data, insert_Junction_Data, insert_Messages_Data

# Define environment
ENV = os.getenv('NODE_ENV', 'development')

# Load environment variables from .env file based on the defined environment
dotenv_path = os.path.join(os.path.dirname(__file__), f'.env.{ENV}')
load_dotenv(dotenv_path=dotenv_path)

config = {}

# Configure the connection pool for production environment
if ENV == 'production':
    config['dsn'] = os.getenv('DATABASE_URL')
    config['maxconn'] = 2

print(ENV)

# Create the connection pool
try:
    connection_pool = pool.SimpleConnectionPool(1, config.get('maxconn', 10), dsn=config.get('dsn'))
    print("Connection pool created successfully")
except Exception as e:
    print(f"Error creating connection pool: {e}")

# Usage example
def get_connection():
    if connection_pool:
        return connection_pool.getconn()
    else:
        raise Exception('Connection pool is not initialized')

def release_connection(conn):
    if connection_pool:
        connection_pool.putconn(conn)

# Example usage
if __name__ == "__main__":
    try:
        conn = get_connection()
        # Use the connection
        release_connection(conn)
    except Exception as e:
        print(f"Error: {e}")

def connect():
    """ Connect to the PostgreSQL database server using connection pool """
    try:
        # Get a connection from the pool
        conn = get_connection()
        print('Connected to the PostgreSQL server.')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    try:
        conn = connect()
        create_tables(conn)  # Pass the connection to the function
        insert_User_Data(conn)  # Pass the connection to the function
        insert_Event_Data(conn)  # Pass the connection to the function
        insert_Junction_Data(conn)  # Pass the connection to the function
        insert_Messages_Data(conn)  # Pass the connection to the function
    finally:
        release_connection(conn)
