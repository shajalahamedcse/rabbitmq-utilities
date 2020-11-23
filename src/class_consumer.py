from rabbitmq_utilities import ConsumeFromBus
import json
cb = ConsumeFromBus('order','direct','order_report')
consumer = cb.consumer()
def callback(ch, method, properties, body):
    print(method)
    
    payload = json.loads(body)
    print(type(payload))

    print(' [x] Notifying {}'.format(payload['user_email']))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
consumer.basic_consume(cb._queue_name,callback)
consumer.start_consuming()