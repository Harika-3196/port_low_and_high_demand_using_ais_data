import psycopg2
import pandas as pd
from db.connection import get_connection
from scripts.query_port_coordinates import get_long_beach_port


#this code snippet retrieves AIS data for cargo vessels within a bounding box around a specified port from a database.
def get_cargo_vessels_within_bounding_box(main_port_name:str,port_code: str, width: float, height: float, cargo_vessel_types: list) -> pd.DataFrame:
    """
    Retrieve AIS data for cargo vessels within a bounding box around a specified port.

    Args:
        port_code (str): The code of the port to get data for.
        width (float): The width of the bounding box in nautical miles.
        height (float): The height of the bounding box in nautical miles.
        cargo_vessel_types (list): A list of cargo vessel types to filter the data for.

    Returns:
        pandas.DataFrame: The AIS data for cargo vessels within the bounding box.

    Raises:
        ValueError: If the port coordinates cannot be retrieved.
    """

    # Get port coordinates from query_port_coordinates.py
    port_info = get_long_beach_port(main_port_name=main_port_name)
    
    if not port_info:
        raise ValueError(f"Failed to retrieve coordinates for port code: {port_code}")

    # Extract the latitude and longitude of the port from the dictionary
    center_lat = port_info["Latitude"] # type: ignore
    center_lon = port_info["Longitude"] # type: ignore

    # Calculate the bounding box coordinates
    lat_min = center_lat - (height / 2) # type: ignore
    lat_max = center_lat + (height / 2) # type: ignore
    lon_min = center_lon - (width / 2) # type: ignore
    lon_max = center_lon + (width / 2) # type: ignore

    # SQL query to filter AIS data within the bounding box and for cargo vessels
    query = """
        SELECT *
        FROM public.ais_data
        WHERE "LAT" BETWEEN %s AND %s
          AND "LON" BETWEEN %s AND %s
          AND "VesselType" IN %s
    """

    # Connect to the database
    connection = get_connection()
    if connection is None:
        return pd.DataFrame()  # Return an empty DataFrame on failure

    cursor = connection.cursor()

    # Execute the query with parameters
    cursor.execute(query, (lat_min, lat_max, lon_min, lon_max, tuple(cargo_vessel_types)))

    # Fetch all matching rows
    results = cursor.fetchall()

    # Get column names from cursor
    column_names = [desc[0] for desc in cursor.description] # type: ignore

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=column_names)

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return df

def count_unique_vessels_by_time(main_port_name:str,port_code: str, width: float, height: float, cargo_vessel_types: list, time_interval: str = 'h') -> pd.DataFrame:
    """
    Count unique vessels in a given time interval within a bounding box around a specified port.

    Args:
        port_code (str): The code of the port to get data for.
        width (float): The width of the bounding box in nautical miles.
        height (float): The height of the bounding box in nautical miles.
        cargo_vessel_types (list): A list of cargo vessel types to filter the data for.
        time_interval (str, optional): The time interval to resample the data by. Defaults to 'h' but can use daily or weekly .

    Returns:
        pandas.DataFrame: The count of unique vessels in the given time interval.
    """
    # Get the filtered DataFrame using the bounding box
    df = get_cargo_vessels_within_bounding_box(main_port_name,port_code, width, height, cargo_vessel_types)
    print("Total vessels obtained after bounding box filter",len(df))
    
    if df.empty:
        return df  # Return empty DataFrame if no data

    # Ensure the 'BaseDateTime' column is in datetime format
    df['BaseDateTime'] = pd.to_datetime(df['BaseDateTime'])
    
    # Set the 'BaseDateTime' as the index
    df.set_index('BaseDateTime', inplace=True)
    
    # Resample the data by the given time interval and count unique vessels
    unique_vessels_count = df.resample(time_interval).agg({'MMSI': pd.Series.nunique}).rename(columns={'MMSI': 'UniqueVessels'}) # type: ignore
   
    
    # Reset the index to get the 'DateTime' column
    unique_vessels_count.reset_index(inplace=True)
    
    return unique_vessels_count

