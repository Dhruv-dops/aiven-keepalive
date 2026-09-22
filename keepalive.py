import os
import mysql.connector

connection = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    ssl_disabled=False
)

cursor = connection.cursor()

cursor.execute("SELECT 1")

result = cursor.fetchone()

print("Aiven MySQL keep-alive:", result)

cursor.close()
connection.close()
