import pika
import time
from pymongo import MongoClient

print('Start')
time.sleep(10)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))
channel = connection.channel()
channel.queue_declare(queue='hello')

client = MongoClient(host='database', port=27017)
db = client.mydb
collection = db.mycoll

print('Wait')
def callback(ch, method, properties, body):
    collection.save({"massage":body})

channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
print('End')
