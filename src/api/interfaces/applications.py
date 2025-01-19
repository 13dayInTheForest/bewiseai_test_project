from abc import ABC, abstractmethod

from src.core.schemas.applications import CreateApplicationSchema, ApplicationSchema


class IApplicationsService(ABC):
    @abstractmethod
    async def create_application(self,
                                 application: CreateApplicationSchema
                                 ) -> ApplicationSchema: ...

    @abstractmethod
    async def get_page(self,
                       username: str = None,
                       page: int = 1,
                       size: int = 20): ...
