import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='inventory_queue')
# channel.queue_declare(queue='op_queue')

# Collect input from the user
# name = input("Enter name: ")
# price = float(input("Enter price: "))

# for stock management
# item_to_be_shipped = input("Enter ITEM name : ")
# quantity_to_be_sent = int(input("Enter the quantity to be shipped : "))

# Create a dictionary representing the item data
# item_data = {'name': name, 'price': price}

# shipping_data = {'name':item_to_be_shipped,'quantity':quantity_to_be_sent}
# ordering_data = {'name': item_to_be_ordered, 'quantity': quantity_to_process}

orders = []
n = int(input("Number of items being ordered: "))
for i in range(n):
    name = input("Enter ITEM name : ")
    quantity = int(input("Enter AMOUNT of item to be ordered: "))
    orders.append({'name':name, 'quantity': quantity})

print(orders)



# Convert the item data to JSON format
# message_body_consumerone = json.dumps(item_data)

# message_body_consumertwo = json.dumps(shipping_data)

message_body_consumerfour = json.dumps({'n': n, 'orders': orders})

# Publish the message to the RabbitMQ queue
#channel.basic_publish(exchange='', routing_key='inventory_queue', body=message_body_consumerone)
# channel.basic_publish(exchange='', routing_key='shipping_queue', body=message_body_consumertwo)
channel.basic_publish(exchange='', routing_key='op_queue', body=message_body_consumerfour)

print("Sent item data to RabbitMQ")

# Close the connection
connection.close()
