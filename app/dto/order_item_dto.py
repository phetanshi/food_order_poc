from pydantic import BaseModel


from decimal import Decimal


class OrderItemDto(BaseModel):
    food_name: str
    quantity: int
    unit_price: Decimal