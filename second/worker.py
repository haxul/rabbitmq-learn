#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rust', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    sec = int(body)
    time.sleep(sec)
    print("DONE")


channel.basic_qos(prefetch_count=1)
channel.basic_consume('hello', callback)
channel.start_consuming()
