from app.dto import ChatResult
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class GreetingHandler(BaseIntentHandler):
    def __init__(self, menu_resolver: MenuResolverService):
        self.menu_resolver: MenuResolverService = menu_resolver

    async def show_menu(self):
        menu = await self.menu_resolver.get_menu()
        menu_text = "\n".join(
            f"• {item.food_item_name} - ₹{item.food_price}"
            for item in menu
        )
        return menu_text
    
    async def handle(self, context: HandlerContext) -> ChatResult:
        menu_text = await self.show_menu()
        greeting = (
            "Hello! 👋\n\n"
            "Welcome to Nahansh Food Services.\n\n"
            "Here's today's menu:\n\n"
            f"{menu_text}\n\n"
            "How can I help you?"
        )
        return ChatResult(message=greeting)
