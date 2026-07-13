from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.order_service import OrderService
from app.services.handlers.handler_context import HandlerContext


class ConfirmOrderHandler(BaseIntentHandler):
    def __init__(self, cart_service, order_service):
        self.cart_service: CartService = cart_service
        self.order_service: OrderService = order_service

    async def handle(self, context: HandlerContext) -> ChatResult:
        if context.conversation.cart.is_empty:
            reply = "Your cart is empty."
        else:
            order = await self.order_service.place_order(context.conversation.cart)
            self.cart_service.clear(context.conversation.cart)
            reply = (
                f"Thank you!\n\n"
                f"Order Id : {order.order_id}\n"
                f"Total : ₹{order.total}"
            )
        return ChatResult(message=reply)
