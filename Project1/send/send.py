import pika
import time
import sys

print('Start')
time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))

channel = connection.channel()
channel.queue_declare(queue='hello')

while (True):
    line = input("> ")
    channel.basic_publish(exchange='', routing_key='hello', body=line)
    print('Done')

connection.close()
print('End')
