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
    # This is pure garbage. Yes I wrote it. And I will clean it up.
    
    def __init__(self,exchange,routing_key,exchange_type):
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
        

class ConsumeFromBus(MessageBusBase):
    def __init__(self,exchange,routing_key,queue_name):
        super(ConsumeFromBus,self).__init__(exchange,routing_key)
        self._queue_name= queue_name
        self._queue = self._queue_bind_to_consume()
        
        
    def _queue_bind_to_consume(self):
        _consume_channel = self._connection.channel()
        _queue = _consume_channel.queue_declare(self._queue_name)
        _consume_channel.queue_bind(
            exchange=self._exchange,
            queue=self._queue_name,
            routing_key=self._routing_key
        )
        return _consume_channel
    
    def consumer(self):
        return self._queue_bind_to_consume()
        
        
        
        
        
        
    
        