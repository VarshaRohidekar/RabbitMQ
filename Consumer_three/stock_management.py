import pika
import mysql.connector
import json

# Connect to MySQL database
mysql_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='newyork1176',
    database='inventory',
    autocommit = 'true'
)
mysql_cursor = mysql_connection.cursor()

def callback(ch, method, properties, body):
    # Decode the JSON message received from producer
    message_data = json.loads(body.decode())
    print(message_data)

    # Extract name and price from the message
    name = message_data['name']
    quantity = int(message_data['quantity'])

    mysql_cursor.execute("""SELECT item_id, quantity FROM stock NATURAL JOIN items WHERE items.name = %(name)s""", {'name': name})
    present_quantity = mysql_cursor.fetchall()
    i = present_quantity[0][0]
    q = int(present_quantity[0][1])
    print(q - quantity)
    n = q - quantity
    print(i)

    mysql_cursor.execute("""UPDATE stock SET quantity = %(new_quantity)s WHERE item_id=%(id)s""", {'id': i, 'new_quantity': n})
        
    # mysql_cursor.execute('INSERT INTO items (name, price) VALUES (%s, %s)', (name, quantity))
    mysql_connection.commit()

    # print(f"Inserted into MySQL: Name: {name}, Price: {price}")

    # # Acknowledge that the message has been processed
    ch.basic_ack(delivery_tag=method.delivery_tag)

    # # Stop consuming after processing a certain number of messages
    # global messages_received
    # messages_received += 1
    # if messages_received >= 20:
    ch.stop_consuming()

# Connect to RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = rabbitmq_connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='shipping_queue')

# Set up consumer parameters
messages_received = 0
channel.basic_consume(queue='shipping_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# Close connections
mysql_cursor.close()
mysql_connection.close()
rabbitmq_connection.close()
