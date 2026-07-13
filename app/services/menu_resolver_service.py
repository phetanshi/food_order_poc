from app.dto import LlmResponse
from app.repositories import FoodRepository
from app.utils.fuzzy_match import FuzzyMatcher
from app.domain.resolved_menu_item import ResolvedMenuItem


class MenuResolverService:

    def __init__(self, food_repository: FoodRepository):
        self.food_repository = food_repository

    async def get_menu(self):
        return await self.food_repository.get_active_menu()

    async def resolve_food_item(self, name: str):
        menu = await self.food_repository.get_active_menu()
        menu_lookup = {
            item.food_item_name: item
            for item in menu
        }

        menu_names = list(menu_lookup.keys())
        best_match = FuzzyMatcher.find_best_match(user_input=name,choices=menu_names)

        if best_match is None:
            return None

        return menu_lookup[best_match]
    
    async def resolve_entities(self, llm_response: LlmResponse) -> tuple[list[ResolvedMenuItem], list[str]]:
        resolved = []
        unavailable = []
        menu = await self.food_repository.get_active_menu()
        lookup = {
            item.food_item_name: item
            for item in menu
        }

        menu_names = list(lookup.keys())
        for entity in llm_response.food_items:
            best_match = FuzzyMatcher.find_best_match(entity.name, menu_names)

            if best_match is None:
                unavailable.append(entity.name)
                continue

            db_item = lookup[best_match]

            resolved.append(
                ResolvedMenuItem(
                        original_name=entity.name,                 # What the user typed
                        resolved_name=db_item.food_item_name,      # What we matched in DB
                        food_item_id=db_item.food_item_id,
                        unit_price=db_item.food_price,
                        quantity=entity.quantity
                )
            )

        return resolved, unavailable