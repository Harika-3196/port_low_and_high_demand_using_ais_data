from typing import Dict, Union
import psycopg2
from db.connection import get_connection



def get_long_beach_port(main_port_name: str) -> Union[Dict[str, str], None]:
    """
    Retrieves the coordinates of the specified main port from the port_coordinates table in the database.

    Args:
        main_port_name (str): The name of the main port to retrieve coordinates for. Defaults to 'Long Beach'.

    Returns:
        Union[Dict[str, str], None]: A dictionary containing the coordinates of the main port if found, None otherwise.
    """
    try:
        # Establish connection
        connection = get_connection()
        if connection is None:
            return None

        cursor = connection.cursor()

        # SQL query to select the row
        query = """
            SELECT "Main Port Name", "UN/LOCODE", "Latitude", "Longitude"
            FROM port_coordinates
            WHERE "Main Port Name" = %s;
        """

        # Execute the query with parameter
        cursor.execute(query, (main_port_name,))

        # Fetch the result
        column_names = [desc[0] for desc in cursor.description]
        row = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Check if a row is found
        if row is None:
            return None

        # Return the result as a dictionary
        return dict(zip(column_names, row))

    except psycopg2.Error as e:
        # Print an error message if there was an error connecting to the database
        print("Error connecting to the database:", e)
        return None



