from app.dto import ChatResult
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class ShowMenuHandler(BaseIntentHandler):
    def __init__(self, menu_resolver: MenuResolverService):
        self.menu_resolver: MenuResolverService = menu_resolver

    async def handle(self, context: HandlerContext) -> ChatResult:
        menu = await self.menu_resolver.get_menu()
        return ChatResult(message="Here is the menu.", data=menu)
