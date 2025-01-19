from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.core.interfaces.applications import IApplicationsRepo
from src.core.database.models import Applications
from src.core.schemas.applications import ApplicationSchema, ApplicationsPageSchema


class ApplicationsRepo(IApplicationsRepo):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> int:
        stmt = insert(Applications).values(**data).returning(Applications.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def commit(self) -> None:
        await self.session.commit()

    # page: страница, size: кол-во элементов на странице
    async def select(self,
                     username: str = None,
                     page: int = 1,
                     size: int = 20
                     ) -> ApplicationsPageSchema:

        stmt = select(Applications).limit(size).offset((page - 1) * size)
        if username is not None:
            stmt = stmt.filter_by(username=username)

        result = await self.session.execute(stmt)
        rows = result.scalars().all()
        return ApplicationsPageSchema(
            result=[ApplicationSchema.from_orm(row) for row in rows],
            page=page,
            size=len(rows)
        )

    async def select_one_by_id(self, user_id: int) -> ApplicationSchema | None:
        stmt = select(Applications).where(Applications.id == user_id)
        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        return ApplicationSchema.from_orm(result) if result is not None else None

