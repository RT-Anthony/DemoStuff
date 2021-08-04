#!/usr/bin/env python
import pika
import sys

def send_message(queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.basic_publish(exchange='', routing_key=queue, body=message)
    connection.close()