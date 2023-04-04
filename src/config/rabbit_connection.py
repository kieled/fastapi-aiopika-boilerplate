import json
import logging
from dataclasses import dataclass
from aio_pika import connect_robust, Message
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from localizations import rabbit
from .base import RABBIT_URL, base_config


@dataclass
class RabbitConnection:
    connection: AbstractRobustConnection | None = None
    channel: AbstractRobustChannel | None = None

    def status(self) -> bool:
        """
            Checks if connection established

            :return: True if connection established
        """
        if self.connection.is_closed or self.channel.is_closed:
            return False
        return True

    async def _clear(self) -> None:
        if not self.channel.is_closed:
            await self.channel.close()
        if not self.connection.is_closed:
            await self.connection.close()

        self.connection = None
        self.channel = None

    async def connect(self) -> None:
        """
        Establish connection with the RabbitMQ

        :return: None
        """
        logging.info(rabbit.CONNECTING)
        try:
            self.connection = await connect_robust(RABBIT_URL)
            self.channel = await self.connection.channel(publisher_confirms=False)
            logging.info(rabbit.CONNECTED)
        except Exception as e:
            await self._clear()
            logging.error(e.__dict__)

    async def disconnect(self) -> None:
        """
        Disconnect and clear connections from RabbitMQ

        :return: None
        """
        await self._clear()

    async def send_messages(
            self,
            messages: list | dict,
            routing_key: str = base_config.RABBITMQ_QUEUE
    ) -> None:
        """
            Public message or messages to the RabbitMQ queue.

            :param messages: list or dict with messages objects.
            :param routing_key: Routing key of RabbitMQ, not required. Tip: the same as in the consumer.
        """
        if not self.channel:
            raise RuntimeError(rabbit.NOT_CONNECTED)

        if isinstance(messages, dict):
            messages = [messages]

        async with self.channel.transaction():
            for message in messages:
                message = Message(
                    body=json.dumps(message).encode()
                )

                await self.channel.default_exchange.publish(
                    message, routing_key=routing_key,
                )


rabbit_connection = RabbitConnection()
