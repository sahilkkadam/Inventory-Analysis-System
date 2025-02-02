import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
        host = 'localhost',
        user = 'inventory_analysis',
        password = 'inventory_analysis123',
        database = 'inventory_analysis_db'
        )
        print("Database connection established")
        return conn
    except Exception as e:
        print(f"Error : {e}")
        return None

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed !!!")

def execute_query(query):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        close_connection(conn)