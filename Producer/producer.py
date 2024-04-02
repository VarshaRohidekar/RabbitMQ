import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='inventory_queue')

# Collect input from the user
# name = input("Enter name: ")
# price = float(input("Enter price: "))

item_to_be_shipped = input("Enter ITEM name : ")
quantity_to_be_sent = int(input("Enter the quantity to be shipped : "))

# Create a dictionary representing the item data
# item_data = {'name': name, 'price': price}

shipping_data = {'name':item_to_be_shipped,'quantity':quantity_to_be_sent}
# Convert the item data to JSON format
# message_body_consumerone = json.dumps(item_data)

message_body_consumertwo = json.dumps(shipping_data)

# Publish the message to the RabbitMQ queue
#channel.basic_publish(exchange='', routing_key='inventory_queue', body=message_body_consumerone)
channel.basic_publish(exchange='', routing_key='shipping_queue', body=message_body_consumertwo)

print("Sent item data to RabbitMQ")

# Close the connection
connection.close()
