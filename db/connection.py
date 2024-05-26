import os
import psycopg2

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



def get_connection() -> psycopg2.extensions.connection:
    """
    Establishes a connection to the PostgreSQL database using the
    parameters specified in the DB_PARAMS dictionary from config/config.py.

    Returns:
        connection (psycopg2.extensions.connection): The database connection object.
        None: If there is an error connecting to the database.
    """

    try:
        # Connect to the database using the parameters from DB_PARAMS
        connection = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
         )
        return connection


    except psycopg2.Error as e:
        # Print an error message if there was an error connecting to the database
        print("Error connecting to the database:", e)
        return None # type: ignore

