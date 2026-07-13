from enum import Enum
from pydantic import BaseModel


class Intent(str, Enum):
    GREETING = "GREETING"
    SHOW_MENU = "SHOW_MENU"
    ADD_ITEM = "ADD_ITEM"
    REMOVE_ITEM = "REMOVE_ITEM"
    UPDATE_QUANTITY = "UPDATE_QUANTITY"
    SHOW_CART = "SHOW_CART"
    SHOW_TOTAL = "SHOW_TOTAL"
    CONFIRM_ORDER = "CONFIRM_ORDER"
    CANCEL_ORDER = "CANCEL_ORDER"
    END_CONVERSATION = "END_CONVERSATION"
    UNKNOWN = "UNKNOWN"

class FoodEntity(BaseModel):
    name: str
    quantity: int = 1

class LlmResponse(BaseModel):
    intent: Intent
    food_items: list[FoodEntity] = []