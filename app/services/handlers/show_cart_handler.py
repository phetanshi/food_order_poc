from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext


class ShowCartHandler(BaseIntentHandler):
    def __init__(self, cart_service: CartService):
        self.cart_service: CartService = cart_service

    async def handle(self, context: HandlerContext) -> ChatResult:
        cart = self.cart_service.to_dto(context.conversation.cart)
        if not cart.items:
            reply = "Your cart is empty."
        else:
            lines = []
            for item in cart.items:
                lines.append(f"{item.food_item_name} x {item.quantity} = ₹{item.total_price}")

            lines.append("")
            lines.append(f"Total : ₹{cart.total}")
            lines.append(f"\nCan I place the order?")
            reply = "\n".join(lines)
        return ChatResult(message=reply, cart=cart)
