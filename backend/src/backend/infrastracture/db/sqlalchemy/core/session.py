from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from backend.src.backend.config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=False,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)