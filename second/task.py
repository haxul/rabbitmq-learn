#!/usr/bin/env python
import pika
import sys

message = sys.argv[1:]

if len(message) == 0:
    raise Exception("error happend")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='rust', durable=True)
channel.basic_publish(exchange='', routing_key='hello',
                      body=message[0], properties=pika.BasicProperties(delivery_mode=2))
print(" [x] Sent 'Hello World!'")
connection.close()
