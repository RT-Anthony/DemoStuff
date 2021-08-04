#!/usr/bin/env python
import pika


def callback(ch, method, properties, body):
    print(" [x] Received {}".format(body))

def callback_two(ch, method, properties, body):
    print(" [!] recieved {}".format(body))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.queue_declare(queue="world")

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)
channel.basic_consume(
    queue="world", on_message_callback=callback_two, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()