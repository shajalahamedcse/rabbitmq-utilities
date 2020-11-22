from rabbitmq_utilities import PublishToBus
import json
pb = PublishToBus('order','direct','order.notify')
order = {
    'user_email': 'john.doe@example.com',
    'product': 'Leather Jacket',
    'quantity': 1
}
pb.publish(json.dumps(order))