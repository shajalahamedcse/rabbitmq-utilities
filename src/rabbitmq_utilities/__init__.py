import pika

from core import Configuration


class MessageBusBase:
    def __init__(self,exchange,routing_key):
        self._url = Configuration.RABBITMQ_URL
        self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
        self._exchange = exchange
        self._routing_key = routing_key
    def _exchange_declare_to_publish(self,exchange_type):
        # Todo 
        # Add exception for null value for exchange and exchange type
        raise NotImplementedError
        # self.channel = self._connection.channel()
        
    def _queue_declare_to_consume(self,queue_name):
        raise NotImplementedError
    
    def _queue_bind_with_exchange(self,routing_key):
        raise NotImplementedError
    
    def publish(self,body):
        raise NotImplementedError
    

class PublishToBus(MessageBusBase):
    def __init__(self,exchange,exchange_type,routing_key):
        super(PublishToBus,self).__init__(exchange,routing_key)
        self._declared_exchange = self._exchange_declare_to_publish(exchange_type)
        
        
    def _exchange_declare_to_publish(self,exchange_type):
        _pub_channel = self._connection.channel()
        _pub_channel.exchange_declare(exchange=self._exchange,exchange_type=exchange_type)
        return _pub_channel
        
    def publish(self, body):
        """
        This method takes body as json data then publish this data 
        to rabbitmq
        """
        self._declared_exchange.basic_publish(exchange=self._exchange,
                                              routing_key=self._routing_key,
                                              body=body
                                              )
        
        
        
    
        