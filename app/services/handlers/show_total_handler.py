from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext


class ShowTotalHandler(BaseIntentHandler):
    def __init__(self, cart_service: CartService):
        self.cart_service = cart_service

    async def handle(self, context: HandlerContext) -> ChatResult:
        total = self.cart_service.calculate_display_total(context.conversation.cart)
        return ChatResult(message=f"Your current total is ₹{total:.2f}.")
