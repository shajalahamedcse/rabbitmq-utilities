import pika
import json
connection = pika.BlockingConnection(pika.URLParameters('amqp://user:password@localhost:5672'))
channel = connection.channel()
queue = channel.queue_declare('order_report')
queue_name = queue.method.queue
channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify'  # binding key
)
def callback(ch, method, properties, body):
    print(method)
    
    payload = json.loads(body)
    print(type(payload))

    print(' [x] Notifying {}'.format(payload['user_email']))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_consume(queue_name,callback)
print(' [*] Waiting for notify messages. To exit press CTRL+C')
channel.start_consuming()