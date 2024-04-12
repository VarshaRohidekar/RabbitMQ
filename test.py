import pika
import mysql.connector
import json
import time

mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='newyork1176',
    database='inventory',
    port=3306,
    autocommit = True
)

mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""SELECT * from items""")

rows = mysql_cursor.fetchall()
for row in rows:
    print(row)
mysql_connection.close()