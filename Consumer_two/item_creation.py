import pika
import mysql.connector
import json
import time

# Connect to MySQL database
mysql_connection = mysql.connector.connect(
    host='mysql',
    user='root',
    password='newyork1176',
    database='inventory',
    autocommit=True,
    port=3306
)
mysql_cursor = mysql_connection.cursor()

def callback(ch, method, properties, body):
    # Decode the JSON message received from producer
    message_data = json.loads(body.decode())

    # Extract name and price from the message
    name = message_data['name']
    price = message_data['price']

    # Insert data into MySQL table
    mysql_cursor.execute('INSERT INTO items (name, price) VALUES (%s, %s)', (name, price))
    

    print(f"Inserted into MySQL: Name: {name}, Price: {price}")

    # Acknowledge that the message has been processed
    time.sleep(20)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    ch.stop_consuming()


# Connect to RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = rabbitmq_connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='item_queue')

# Set up consumer parameters
channel.basic_consume(queue='item_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# Close connections
mysql_cursor.close()
mysql_connection.close()
rabbitmq_connection.close()
