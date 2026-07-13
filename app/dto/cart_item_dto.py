from pydantic import BaseModel


from decimal import Decimal


class CartItemDto(BaseModel):
    food_item_id: int
    food_item_name: str
    quantity: int
    unit_price: Decimal
    total_price: Decimal