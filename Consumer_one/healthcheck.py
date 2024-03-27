import pika
import json

def process_inventory_update(channel, method, properties, body):
    # Parse the JSON message
    message = json.loads(body)
    product_id = message["product_id"]
    quantity = message["quantity"]

    # Print a debug message indicating message reception
    print(f"Received message: Product ID {product_id}, Quantity {quantity}")

    # Simulate processing the update (replace with your actual logic)
    print(f"Processed update for product {product_id} with quantity {quantity}")

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# Declare the queue (same as producer)
channel.queue_declare(queue="inventory_updates")

# Specify the callback function to handle incoming messages
channel.basic_consume(queue="inventory_updates", on_message_callback=process_inventory_update, auto_ack=True)

print("Waiting for messages...")

# Start consuming messages
channel.start_consuming()
