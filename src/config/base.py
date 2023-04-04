from pydantic import BaseSettings


class Base(BaseSettings):
    RABBITMQ_DEFAULT_USER: str = 'user'
    RABBITMQ_DEFAULT_PASS: str = 'password'
    RABBITMQ_LOCAL_HOST_NAME: str = 'rabbit'
    RABBITMQ_LOCAL_PORT: int = 5672
    RABBITMQ_QUEUE: str = 'test_queue'

    POSTGRES_PASSWORD: str = 'admin123'
    POSTGRES_USER: str = 'admin'
    POSTGRES_DB: str = 'main'
    POSTGRES_HOST: str = 'db'
    POSTGRES_PORT: int = 5432

    CLIENT_ORIGIN: str = 'http://localhost:3000'


base_config = Base()

RABBIT_URL = f'amqp://{base_config.RABBITMQ_DEFAULT_USER}:' \
             f'{base_config.RABBITMQ_DEFAULT_PASS}@' \
             f'{base_config.RABBITMQ_LOCAL_HOST_NAME}:' \
             f'{base_config.RABBITMQ_LOCAL_PORT}/'
