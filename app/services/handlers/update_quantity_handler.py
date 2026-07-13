from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class UpdateQuantityHandler(BaseIntentHandler):
    def __init__(self, cart_service: CartService, menu_resolver: MenuResolverService):
        self.cart_service = cart_service
        self.menu_resolver = menu_resolver

    async def handle(self, context: HandlerContext) -> ChatResult:
        resolved_items, unavailable = await self.menu_resolver.resolve_entities(context.llm_response)

        if unavailable:
            return ChatResult(message="Unable to update quantity because some items were not found.")

        for food, qty in resolved_items:
            self.cart_service.update_quantity(context.conversation.cart, food, qty)

        cart = self.cart_service.to_dto(context.conversation.cart)
        return ChatResult(message="Quantity updated successfully.", cart=cart)
