from typing import List, Union

from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.db.models import Order, FoodItemOrder
from app.repositories.base_repository import BaseRepository

class OrderRepository(BaseRepository[Order]):
    def __init__(self, session):
        super().__init__(session, Order)

    async def create_order(self, order: Order):
        self.session.add(order)
        await self.session.flush()
        return order

    async def add_order_items(self, item: Union[FoodItemOrder, List[FoodItemOrder]]):
        if isinstance(item, list):
            # ✅ Correct way to add multiple ORM objects
            self.session.add_all(item)
        else:
            # ✅ Single object case
            self.session.add(item)

    async def get_order(self, order_id: int):
        result = await self.session.execute(
            select(Order)
            .options(selectinload(Order.food_items))
            .where(Order.order_id == order_id)
        )
        return result.scalar_one_or_none()