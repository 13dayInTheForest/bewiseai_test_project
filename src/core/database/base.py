from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.core.database.config import settings
from src.core.database.models import Base
from src.core.exceptions.base_exc import ConnectFailedException
from sqlalchemy import text

async_engine = create_async_engine(
    settings.get_db_url,
    pool_size=30,
    max_overflow=20,
    pool_timeout=10,
    echo=True
)
async_session = async_sessionmaker(bind=async_engine)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_tables() -> None:
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        await connect.commit()


async def drop_database():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.commit()


async def heath_check() -> None:
    async_engine.echo = True
    try:
        async with async_engine.connect() as connect:
            await connect.execute(text('SELECT 1'))
    except Exception as ex:
        raise ex
    async_engine.echo = False

