from pydantic import BaseModel

from app.dto.cart_dto import CartDto
from app.dto.order_response_dto import OrderResponseDto


class ChatResult(BaseModel):
    """
    Internal result returned by intent handlers.
    ChatService converts this into the API response.
    """
    message: str
    cart: CartDto | None = None
    order: OrderResponseDto | None = None