import pika
import sys
import time

def check_rabbitmq_health():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672))
        connection.close()
        return True
    except pika.exceptions.AMQPConnectionError:
        return False

def main():
    retries = 5
    interval = 10  # seconds

    for _ in range(retries):
        if check_rabbitmq_health():
            print("RabbitMQ is up and running.")
            sys.exit(0)  # Exit with success status
        else:
            print("RabbitMQ is not reachable. Retrying in {} seconds...".format(interval))
            time.sleep(interval)

    print("RabbitMQ could not be reached after {} retries. Exiting.".format(retries))
    sys.exit(1)  # Exit with failure status

if __name__ == "__main__":
    main()
