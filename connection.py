import mysql.connector
import csv

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

def execute_query(query, output_csv):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        headers = [i[0] for i in cursor.description]

        with open(output_csv, mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(result)
        print(f"Query results saved to {output_csv}")

        for row in result:
            print(row)
    except Exception as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        close_connection(conn)