from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from src.api.routers.applications import router as app_router
from src.core.database.base import heath_check, async_engine, create_tables, drop_database
from src.core.kafka.base import message_broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    await heath_check()
    await message_broker.start()
    await create_tables()
    try:
        yield
    finally:
        await drop_database()
        await message_broker.stop()
        # Чистим все соединения при завершении работы
        await async_engine.dispose()


app = FastAPI(
    title='Test Project',
    lifespan=lifespan
)
app.include_router(app_router)


@app.get('/')
async def redirect_from_main_to_docs():
    # С главной страницы переводим на документацию (i mean, why not)
    return RedirectResponse('/docs')


if __name__ == '__main__':
    from uvicorn import run
    run("src.main:app", port=8000, host='127.0.0.1', reload=True)
