from aiokafka import AIOKafkaProducer

from src.core.exceptions.base_exc import MessageBrokerNotImplement
from src.core.interfaces.broker import IMessageBroker
from src.core.schemas.applications import ApplicationSchema


class KafkaProducer(IMessageBroker):
    def __init__(self, bootstrap_server: str, topic: str):
        self.bootstrap_server = bootstrap_server
        self.topic = topic
        self.producer: AIOKafkaProducer | None = None

    async def start(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_server)
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()

    async def send_message(self, message: ApplicationSchema) -> bool:
        if self.producer is None:
            raise MessageBrokerNotImplement
        try:
            await self.producer.send_and_wait(value=message.json().encode('utf-8'), topic=self.topic)
            return True
        except Exception as e:
            raise e
