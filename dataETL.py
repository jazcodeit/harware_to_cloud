import pandas as pd
import json
import os
import pyodbc

# Load environment variables
server = os.getenv('DATABASE_SERVER')
database = os.getenv('DATABASE_NAME')
username = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')
port = os.getenv('DATABASE_PORT')
table_name = os.getenv('DATABASE_TABLE')
driver = '{ODBC Driver 17 for SQL Server}'

# Extract data from JSON file
data = pd.read_json('sensorData.json')

# Data Cleaning

# Connection String for Azure SQL Database
connection_str = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'


with pyodbc.connect(connection_str) as conn:
    cursor = conn.cursor()
    
    # Load data into Azure SQL Database
    sql = "INSERT INTO {table_name} (column1, column2) VALUES (?, ?)"
    values = ("Example Data", 123)
    
    # Execute and commit
    cursor.execute(sql, values)
    conn.commit()


print(data)