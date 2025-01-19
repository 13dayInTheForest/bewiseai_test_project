from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.core.repositories.applications import ApplicationsRepo
from src.core.database.base import get_async_session


async def get_applications_repo(session: AsyncSession = Depends(get_async_session)):
    return ApplicationsRepo(session)
