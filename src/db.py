# database connection and utility functions for EmploiQL
# this module handles all communication between python and postgresql
from typing import Any
import os
import psycopg2

# special cursor that returns query results as dictionaries
from psycopg2.extras import RealDictCursor

def get_connection():
    """create and return a database connection"""
    # establishes a new database session
    # it returns a connection object that we use for all database operations
    # host - where the database server is running ("localhost" means your own computer)
    # port - the network port postgresql listens on (5432 is the default)
    connection = psycopg2.connect(
        dbname="EmploiQL",
        user=os.getenv("USER"), # os.getenv() reads environment variables from system
        host="localhost",
        port="5432"
    )
    return connection

# test to verify the database connection works
if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()
    # standard way to test if the database is responding
    # it doesnt read any tables, just asks postgresql to return the number 1
    cursor.execute("SELECT 1")
    
    # fetchone() returns a tuple like (1,)
    result = cursor.fetchone()
    test_value = result[0]
    
    if test_value == 1:
        print("connected successfully to EmploiQL database")
    else:
        print("connection test failed")
    
    # always clean up when done
    cursor.close()
    connection.close()