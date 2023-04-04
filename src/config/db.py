from asyncio import current_task
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import \
    create_async_engine, \
    async_sessionmaker, \
    async_scoped_session

from .base import base_config

DATABASE_URL = f"postgresql+asyncpg://{base_config.POSTGRES_USER}:" \
               f"{base_config.POSTGRES_PASSWORD}" \
               f"@{base_config.POSTGRES_HOST}" \
               f":{base_config.POSTGRES_PORT}" \
               f"/{base_config.POSTGRES_DB}"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)


@asynccontextmanager
async def scoped_session():
    scoped_factory = async_scoped_session(
        async_sessionmaker(engine, expire_on_commit=False),
        scopefunc=current_task,
    )
    try:
        async with scoped_factory() as s:
            yield s
    finally:
        await scoped_factory.remove()
