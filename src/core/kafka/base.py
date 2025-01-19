from .producer import KafkaProducer
from ..database.config import settings


message_broker = KafkaProducer(settings.KAFKA_BOOTSTRAP_SERVERS, settings.KAFKA_TOPIC)


async def broker_healthcheck():
    pass

