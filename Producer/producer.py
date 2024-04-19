import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='inventory_queue')
# channel.queue_declare(queue='op_queue')

# Consumer four
# Read input data from JSON file
with open('input_data.json', 'r') as file:
    input_data = json.load(file)

orders = input_data['orders']
n = input_data['n']

print(orders)

# Convert the input data to JSON format
message_body_consumerfour = json.dumps({'n': n, 'orders': orders})

# Publish the message to the RabbitMQ queue
channel.basic_publish(exchange='', routing_key='op_queue', body=message_body_consumerfour)

print("Sent item data to RabbitMQ")

# Close the connection
connection.close()
