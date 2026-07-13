from typing import Generic, TypeVar, Type
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import Base

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):

    def __init__(
        self,
        session: AsyncSession,
        model: Type[T]
    ):
        self.session = session
        self.model = model

    async def get_by_id(self, id: int):

        return await self.session.get(
            self.model,
            id
        )

    async def get_all(self):

        result = await self.session.execute(
            select(self.model)
        )

        return result.scalars().all()

    async def add(self, entity: T):

        self.session.add(entity)

        await self.session.flush()

        return entity

    async def delete(self, entity: T):

        await self.session.delete(entity)

    async def save(self):

        await self.session.commit()

    async def rollback(self):

        await self.session.rollback()