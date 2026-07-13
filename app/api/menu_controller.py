from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_food_repository
from app.repositories.food_repository import FoodRepository

menu_router = APIRouter(
    prefix="/api/menu",
    tags=["Menu"],
)


@menu_router.get("")
async def get_menu(repository: FoodRepository = Depends(get_food_repository)):
    menu = await repository.get_active_menu()
    return menu