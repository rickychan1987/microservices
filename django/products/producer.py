import pika

params = pika.URLParameters('amqps://ebkxcskx:e7zDPjFJsDRrYtTgvyY8y0ukihnegHig@gerbil.rmq.cloudamqp.com/ebkxcskx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')