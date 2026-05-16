import pandas as pd
import json
from dotenv import load_dotenv
import os
import pymssql

# Load environment variables
load_dotenv()
port = 1433 # Default port for SQL Server

# Retrieve .env values
try:
    server = os.environ['DATABASE_SERVER']
    database = os.environ['DATABASE_NAME']
    username = os.environ['DATABASE_USER']
    password = os.environ['DATABASE_PASSWORD']
    table_name = os.environ['DATABASE_TABLE']
except Exception as e:
    print(f"Error loading environment variables: {e}")
    exit(1)



# Extract data from JSON file
data = pd.read_json('sensorData.json')

# Data Cleaning


try:
    # Connect to the database using pymssql
    conn = pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database,
        port=port
    )

    # Initialize cursor object
    cursor = conn.cursor()

    query = f"SELECT @@VERSION"

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

except pymssql.Error as e:
    print(f"An error occurred: {e}")