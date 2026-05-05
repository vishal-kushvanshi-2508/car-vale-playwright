
import mysql.connector




db_setting = {
    "host" : "localhost", 
    "user" : "root",
    "password" : "actowiz",
    "port" : "3306",
    "database" : "car_vale_request_db_second"
}
connection = mysql.connector.connect(**db_setting)


cursor = connection.cursor()


def fetch_car_url():
    query = """select * from cars_url"""

    cursor.execute(query)

    rows = cursor.fetchall()
    # print(rows)

    car_url_list = []
    for data in rows:
        car_url_list.append({
            "id" : data[0],
            "brand_name" : data[1],
            "brand_url" : data[2],
            "car_name" : data[3],
            "car_url" : data[4],
            "status" : data[5]
        })
    return car_url_list




