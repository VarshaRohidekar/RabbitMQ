import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="inventory_updates")

message = {"product_id": 123, "quantity": 5}
channel.basic_publish(exchange="", routing_key="inventory_updates", body=json.dumps(message))

connection.close()