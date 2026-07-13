import asyncio
from sqlalchemy import text
from db.database import engine


async def test():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 123"))
        print(result.scalar())

asyncio.run(test())