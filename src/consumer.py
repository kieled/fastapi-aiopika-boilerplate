import asyncio
import logging
import aio_pika

from config import base_config, RABBIT_URL
from pika import message_router
from localizations import consumer

PARALLEL_TASKS = 10

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("logs/consumer.log"),
        logging.StreamHandler()
    ]
)


async def main() -> None:
    connection = await aio_pika.connect_robust(RABBIT_URL)

    queue_name = base_config.RABBITMQ_QUEUE

    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=PARALLEL_TASKS)
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        logging.info(consumer.STARTED)

        await queue.consume(message_router)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    logging.info(consumer.STARTING)
    asyncio.run(main())
