from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
import urllib

from app.core.config import get_settings

settings = get_settings()

connection_string = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={settings.db_server};"
    f"Database={settings.db_database};"
    f"UID={settings.db_username};"
    f"PWD={settings.db_password};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

params = urllib.parse.quote_plus(connection_string)
# engine = create_async_engine(f"mssql+pyodbc:///?odbc_connect={params}", echo=True, future=True, pool_pre_ping=True)
engine = create_async_engine(f"mssql+aioodbc:///?odbc_connect={params}", echo=True, future=True, pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session