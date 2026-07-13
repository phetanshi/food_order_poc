from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class RemoveItemHandler(BaseIntentHandler):
    def __init__(self, cart_service: CartService, menu_resolver: MenuResolverService):
        self.cart_service: CartService = cart_service
        self.menu_resolver: MenuResolverService = menu_resolver

    async def handle(self, context: HandlerContext) -> ChatResult:
        resolved_items, unavailable = await self.menu_resolver.resolve_entities(context.llm_response)

        if unavailable:
            return ChatResult(message=f"Sorry, we couldn't find: {', '.join(unavailable)}.")

        for menu_item in resolved_items:
            self.cart_service.remove_item(cart=context.conversation.cart,menu_item=menu_item,quantity=menu_item.quantity)

        cart = self.cart_service.to_dto(context.conversation.cart)
        return ChatResult(message="Item(s) removed successfully.", cart=cart)
