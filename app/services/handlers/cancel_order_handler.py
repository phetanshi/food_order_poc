from app.dto import ChatResult
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext


class CancelOrderHandler(BaseIntentHandler):
    def __init__(self, cart_service):
        self.cart_service = cart_service

    async def handle(self, context: HandlerContext) -> ChatResult:
        self.cart_service.clear(context.conversation.cart)
        return ChatResult(message="Your order has been cancelled.")
