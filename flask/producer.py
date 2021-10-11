import pika, json

params = pika.URLParameters('amqps://ebkxcskx:e7zDPjFJsDRrYtTgvyY8y0ukihnegHig@gerbil.rmq.cloudamqp.com/ebkxcskx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)