

from typing import List, Tuple
import mysql.connector # Must include .connector


table_name = "cars_url"
DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "actowiz",
    "port" : "3306",
    "database" : "car_vale_request_db_second"
}

def get_connection():
    try:
        ## here ** is unpacking DB_CONFIG dictionary.
        connection = mysql.connector.connect(**DB_CONFIG)
        ## it is protect to autocommit
        connection.autocommit = False
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

def create_db():
    connection = get_connection()
    # connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS car_vale_request_db_four;")
    connection.commit()
    connection.close()
# create_db()



def fetch_cars_url_table():
    connection = get_connection()
    cursor = connection.cursor()
    # query = f"SELECT * FROM {table_name} WHERE status = 'pending' ;"
    query = f"SELECT * FROM {table_name}  ;"
 
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        data = {
            "id": row[0],
            "brand_name": row[1],
            "brand_url": row[2],
            "car_name": row[3],
            "car_url": row[4],
            "status": row[5]
        }
        result.append(data)

    cursor.close()
    connection.close()
    return result
