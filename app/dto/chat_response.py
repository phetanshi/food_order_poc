from pydantic import BaseModel

from app.dto.cart_dto import CartDto
from app.dto.order_response_dto import OrderResponseDto
from app.exceptions.error_code import ErrorCode


class ChatResponse(BaseModel):
    reply: str
    cart: CartDto | None = None
    order: OrderResponseDto | None = None
    error_code: ErrorCode | None = None