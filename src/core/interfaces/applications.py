from abc import ABC, abstractmethod

from src.core.schemas.applications import ApplicationSchema, ApplicationsPageSchema


class IApplicationsRepo(ABC):
    @abstractmethod
    async def create(self, data: dict) -> int: ...

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...

    @abstractmethod
    async def select_one_by_id(self, user_id: int) -> ApplicationSchema | None: ...

    @abstractmethod
    async def select(self,
                     username: str = None,
                     page: int = 1,
                     size: int = 20
                     ) -> ApplicationsPageSchema: ...
