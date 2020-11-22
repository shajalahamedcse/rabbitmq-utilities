import os

class RabbitMQConfig:
    _rabbitmq_host = os.getenv("RABBITMQ_HOST", "")
    _rabbitmq_port = int(os.getenv("RABBITMQ_PORT", "6379"))
    _rabbitmq_user = os.getenv("RABBITMQ_USER","user")
    _rabbitmq_password = os.getenv("RABBITMQ_PASSWORD", "password")
    

class RabbitMQURLConfig:
    """
    Connection Format :  amqp://user:password@localhost:5672
    """
    _rabbitmq_url: str = f"aqmp://{RabbitMQConfig._rabbitmq_user}:{RabbitMQConfig._rabbitmq_password}@{RabbitMQConfig._rabbitmq_host}:{RabbitMQConfig._rabbitmq_port}"
    
    
    
class Configuration:
    # Rabbitmq Config
    RABBITMQ_URL: str = RabbitMQURLConfig._rabbitmq_url
