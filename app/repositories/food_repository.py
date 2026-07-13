from sqlalchemy import func, select
from app.db.models import FoodItem
from app.repositories.base_repository import BaseRepository
from app.cache.menu_cache import menu_cache


class FoodRepository(BaseRepository[FoodItem]):
    def __init__(self, session):
        super().__init__(session, FoodItem)

    async def get_active_menu(self):
        if 'active_menu' in menu_cache:
            return menu_cache['active_menu']

        result = await self.session.execute(
            select(FoodItem)
            .where(FoodItem.is_active == True)
            .order_by(FoodItem.food_item_name)
        )
        menu = result.scalars().all()
        menu_cache['active_menu'] = menu
        return menu

    async def get_by_name(self, food_name: str):
        result = await self.session.execute(
            select(FoodItem)
            .where(func.lower(FoodItem.food_item_name) == food_name.lower())
            .where(FoodItem.is_active == True)
        )
        return result.scalar_one_or_none()

    async def exists(self, food_name: str):
        food = await self.get_by_name(food_name)
        return food is not None
    
    async def get_by_ids(self, food_item_ids: list[int]) -> list[FoodItem]:
        """
        Returns all active food items for the supplied ids.
        """

        if not food_item_ids:
            return []
        
        stmt = (
            select(FoodItem)
            .where(
                FoodItem.food_item_id.in_(food_item_ids),
                FoodItem.is_active == True,
            )
        )

        result = await self.session.execute(stmt)
        return result.scalars().all()