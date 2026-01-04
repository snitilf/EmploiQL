import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    """create and return a database connection"""
    return psycopg2.connect(
        dbname="EmploiQL",
        user=os.getenv("Snitil"),
        host="localhost",
        port="5432"
    )
    
# test
if __name__ == "__main__":
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1")
    print("connected to the database" if cur.fetchone()[0] == 1 else "failed to connect to the database")
    conn.close()