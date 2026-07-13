from app.dto.order_item_dto import OrderItemDto
from pydantic import BaseModel
from decimal import Decimal


class OrderResponseDto(BaseModel):
    order_id: int
    items: list[OrderItemDto]
    total: Decimal
    message: str