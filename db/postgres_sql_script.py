from typing import List
import psycopg2
from db.connection import get_connection



def execute_sql_commands(commands: List[str], use_db_params: bool = True) -> None:
    """
    Executes a list of SQL commands on the database.

    Args:
        commands (List[str]): List of SQL commands to execute.
        use_db_params (bool, optional): Whether to use the default database
            connection for initial setup. Defaults to True.

    Raises:
        Exception: If there is an error executing a SQL command.
        psycopg2.DatabaseError: If there is an error connecting to the database.

    Returns:
        None
    """
    try:
        # Use default database connection for initial setup
        if use_db_params:
            connection = get_connection()
        else:
            print("connection went wrong")
        connection.autocommit = True
        cursor = connection.cursor()
        
        # Execute each SQL command
        for command in commands:
            cursor.execute(command)
            print(f"Executed: {command}")
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Database setup completed successfully.")
    
    # Handle exceptions
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def main() -> None:
    """
    Executes SQL commands for initial database and user creation,
    and for setting up schema and tables within ais_database.

    This function does not take any arguments and does not return anything.
    """
    # SQL commands for initial database and user creation
    initial_commands: List[str] = [
        "CREATE DATABASE ais_database;",  # Create database
        "CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';",  # Create user
        "GRANT ALL PRIVILEGES ON DATABASE ais_database TO myuser;"  # Grant privileges
    ]

    # SQL commands for setting up schema and tables within ais_database
    ais_commands: List[str] = [
        """
        CREATE TABLE public.ais_data (
            "MMSI" BIGINT,
            "BaseDateTime" TIMESTAMP,
            "LAT" FLOAT,
            "LON" FLOAT,
            "SOG" FLOAT,
            "COG" FLOAT,
            "Heading" FLOAT,
            "VesselName" VARCHAR(255),
            "IMO" VARCHAR(255),
            "CallSign" VARCHAR(255),
            "VesselType" INT,
            "Status" INT,
            "Length" FLOAT,
            "Width" FLOAT,
            "Draft" FLOAT,
            "Cargo" INT,
            "TransceiverClass" CHAR(1)
        );
        """,  # Create ais_data table
        r"\copy ais_data FROM '/data/postgres_data/AIS_2020_01_01.csv' DELIMITER ',' CSV HEADER;",  # Load data to ais_data table
        r"\copy ais_data FROM '/data/postgres_data/AIS_2020_01_02.csv' DELIMITER ',' CSV HEADER;",
        "SELECT COUNT(*) FROM public.ais_data;",  # Check number of rows in ais_data table
        """
        CREATE TABLE public.port_coordinates (
            "OID_" FLOAT,
            "World Port Index Number" FLOAT,
            "Region Name" TEXT,
            "Main Port Name" TEXT,
            "Alternate Port Name" TEXT,
            "UN/LOCODE" TEXT,
            "Country Code" TEXT,
            "World Water Body" TEXT,
            "IHO S-130 Sea Area" TEXT,
            "Sailing Direction or Publication" TEXT,
            "Publication Link" TEXT,
            "Standard Nautical Chart" TEXT,
            "IHO S-57 Electronic Navigational Chart" TEXT,
            "IHO S-101 Electronic Navigational Chart" TEXT,
            "Digital Nautical Chart" TEXT,
            "Tidal Range (m)" REAL,
            "Entrance Width (m)" REAL,
            "Channel Depth (m)" REAL,
            "Anchorage Depth (m)" REAL,
            "Cargo Pier Depth (m)" REAL,
            "Oil Terminal Depth (m)" REAL,
            "Liquified Natural Gas Terminal Depth (m)" REAL,
            "Maximum Vessel Length (m)" REAL,
            "Maximum Vessel Beam (m)" REAL,
            "Maximum Vessel Draft (m)" REAL,
            "Offshore Maximum Vessel Length (m)" REAL,
            "Offshore Maximum Vessel Beam (m)" REAL,
            "Offshore Maximum Vessel Draft (m)" REAL,
            "Harbor Size" TEXT,
            "Harbor Type" TEXT,
            "Harbor Use" TEXT,
            "Shelter Afforded" TEXT,
            "Entrance Restriction - Tide" TEXT,
            "Entrance Restriction - Heavy Swell" TEXT,
            "Entrance Restriction - Ice" TEXT,
            "Entrance Restriction - Other" TEXT,
            "Overhead Limits" TEXT,
            "Underkeel Clearance Management System" TEXT,
            "Good Holding Ground" TEXT,
            "Turning Area" TEXT,
            "Port Security" TEXT,
            "Estimated Time of Arrival Message" TEXT,
            "Quarantine - Pratique" TEXT,
            "Quarantine - Sanitation" TEXT,
            "Quarantine - Other" TEXT,
            "Traffic Separation Scheme" TEXT,
            "Vessel Traffic Service" TEXT,
            "First Port of Entry" TEXT,
            "US Representative" TEXT,
            "Pilotage - Compulsory" TEXT,
            "Pilotage - Available" TEXT,
            "Pilotage - Local Assistance" TEXT,
            "Pilotage - Advisable" TEXT,
            "Tugs - Salvage" TEXT,
            "Tugs - Assistance" TEXT,
            "Communications - Telephone" TEXT,
            "Communications - Telefax" TEXT,
            "Communications - Radio" TEXT,
            "Communications - Radiotelephone" TEXT,
            "Communications - Airport" TEXT,
            "Communications - Rail" TEXT,
            "Search and Rescue" TEXT,
            "NAVAREA" TEXT,
            "Facilities - Wharves" TEXT,
            "Facilities - Anchorage" TEXT,
            "Facilities - Dangerous Cargo Anchorage" TEXT,
            "Facilities - Med Mooring" TEXT,
            "Facilities - Beach Mooring" TEXT,
            "Facilities - Ice Mooring" TEXT,
            "Facilities - Ro-Ro" TEXT,
            "Facilities - Solid Bulk" TEXT,
            "Facilities - Liquid Bulk" TEXT,
            "Facilities - Container" TEXT,
            "Facilities - Breakbulk" TEXT,
            "Facilities - Oil Terminal" TEXT,
            "Facilities - LNG Terminal" TEXT,
            "Facilities - Other" TEXT,
            "Medical Facilities" TEXT,
            "Garbage Disposal" TEXT,
            "Chemical Holding Tank Disposal" TEXT,
            "Degaussing" TEXT,
            "Dirty Ballast Disposal" TEXT,
            "Cranes - Fixed" TEXT,
            "Cranes - Mobile" TEXT,
            "Cranes - Floating" TEXT,
            "Cranes Container" TEXT,
            "Lifts - 100+ Tons" TEXT,
            "Lifts - 50-100 Tons" TEXT,
            "Lifts - 25-49 Tons" TEXT,
            "Lifts - 0-24 Tons" TEXT,
            "Services - Longshoremen" TEXT,
            "Services - Electricity" TEXT,
            "Services - Steam" TEXT,
            "Services - Navigation Equipment" TEXT,
            "Services - Electrical Repair" TEXT,
            "Services - Ice Breaking" TEXT,
            "Services - Diving" TEXT,
            "Supplies - Provisions" TEXT,
            "Supplies - Potable Water" TEXT,
            "Supplies - Fuel Oil" TEXT,
            "Supplies - Diesel Oil" TEXT,
            "Supplies - Aviation Fuel" TEXT,
            "Supplies - Deck" TEXT,
            "Supplies - Engine" TEXT,
            "Repairs" TEXT,
            "Dry Dock" TEXT,
            "Railway" TEXT,
            "Latitude" REAL,
            "Longitude" REAL
        );
        """,  # Create port_coordinates table
        r"\copy port_coordinates FROM 'data/postgres_data/updatedpub.csv' DELIMITER ',' CSV HEADER;",  # Load data to port_coordinates table
        "SELECT COUNT(*) FROM public.port_coordinates;",  # Check number of rows in port_coordinates table
         "GRANT SELECT ON TABLE public.ais_data TO myuser;",
        "GRANT SELECT ON TABLE public.port_coordinates TO myuser;"
    ]

    execute_sql_commands(initial_commands)
    execute_sql_commands(ais_commands, use_db_params=False)


if __name__ == "__main__":
    main()
