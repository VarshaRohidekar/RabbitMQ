import pika
import mysql.connector
import json
import time

mysql_connection = mysql.connector.connect(
    host='mysql',
    user='root',
    password='newyork1176',
    database='inventory',
    port=3306,
    autocommit = True
)
mysql_cursor = mysql_connection.cursor()

def callback(ch, method, properties, body):
    message_data = json.loads(body.decode())

    name = message_data['name']
    quantity = int(message_data['quantity'])

    mysql_cursor.execute("""SELECT item_id, quantity FROM stock NATURAL JOIN items WHERE items.name = %(name)s""", {'name': name})
    present_quantity = mysql_cursor.fetchall()
    q = int(present_quantity[0][1])

    mysql_connection.commit()
    time.sleep(15)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    ch.stop_consuming()

rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = rabbitmq_connection.channel()
channel.queue_declare(queue='shipping_queue')

messages_received = 0
channel.basic_consume(queue='shipping_queue', on_message_callback=callback)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
mysql_cursor.close()
mysql_connection.close()
rabbitmq_connection.close()