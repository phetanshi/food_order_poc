from app.dto.cart_item_dto import CartItemDto
from pydantic import BaseModel
from decimal import Decimal


class CartDto(BaseModel):
    items: list[CartItemDto]
    total: Decimal