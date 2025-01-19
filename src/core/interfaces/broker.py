from abc import ABC, abstractmethod

from src.core.schemas.applications import ApplicationSchema


class IMessageBroker(ABC):
    @abstractmethod
    async def start(self): ...

    @abstractmethod
    async def stop(self): ...

    @abstractmethod
    async def send_message(self, message: ApplicationSchema) -> bool: ...

