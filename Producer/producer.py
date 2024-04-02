import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='inventory_queue')

# Collect input from the user
name = input("Enter name: ")
price = float(input("Enter price: "))

# Create a dictionary representing the item data
item_data = {'name': name, 'price': price}

# Convert the item data to JSON format
message_body = json.dumps(item_data)

# Publish the message to the RabbitMQ queue
channel.basic_publish(exchange='', routing_key='inventory_queue', body=message_body)

print("Sent item data to RabbitMQ")

# Close the connection
connection.close()
