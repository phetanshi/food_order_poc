from app.dto import ChatResult
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class EndConversationHandler(BaseIntentHandler):

    async def handle(self, context: HandlerContext) -> ChatResult:
        return ChatResult(message="Thank you and visit again!")
