import pika 
import json 

connection = pika.BlockingConnection(pika.URLParameters('amqp://user:password@localhost:5672'))
channel = connection.channel()

channel.exchange_declare(exchange='order',exchange_type='direct')

order = {
    'user_email': 'john.doe@example.com',
    'product': 'Leather Jacket',
    'quantity': 1
}

channel.basic_publish(    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'user_email': order['user_email']})
    )

# xs


print(' [x] Sent notify message')
channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order)
)
print(' [x] Sent report message')
connection.close() 