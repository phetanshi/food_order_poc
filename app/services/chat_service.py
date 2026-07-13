from app.dispatcher.intent_dispatcher import IntentDispatcher
from app.domain.conversation import Conversation
from app.dto import ChatResponse
from app.exceptions.error_code import ErrorCode
from app.exceptions.intent_extraction_exception import IntentExtractionException
from app.services.cart_service import CartService
from app.services.conversation_service import ConversationManagerService
from app.services.llm_service import LLMService
from app.services.menu_resolver_service import MenuResolverService
from app.services.order_service import OrderService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.core.logging import logger

class ChatService:
    def __init__(self, 
                 conversation_manager:ConversationManagerService, 
                 llm_service:LLMService, 
                 menu_resolver: MenuResolverService,
                 intent_dispatcher: IntentDispatcher):
        self.conversation_manager = conversation_manager
        self.llm_service = llm_service
        self.menu_resolver = menu_resolver
        self.intent_dispatcher = intent_dispatcher

    async def process_message(self, session_id: str, message: str) -> ChatResponse:
        conversation: Conversation = self.conversation_manager.get_or_create(session_id)
        conversation.add_user_message(message)
        try:
            llm_response = await self.llm_service.extract_intent(conversation.to_prompt(), message)

            print("\n")
            print("=" * 80)
            print(llm_response)
            print("=" * 80)
            print("\n")

            resolved, unavailable = await self.menu_resolver.resolve_entities(llm_response)
            context = HandlerContext(
                conversation=conversation,
                llm_response=llm_response,
                resolved_items=resolved,
                unavailable_items=unavailable
            )
            handler: BaseIntentHandler = self.intent_dispatcher.get_handler(llm_response.intent)
            if handler is None:
                error_msg = f"No handler registered for {llm_response.intent}"
                conversation.add_assistant_message(error_msg)
                return ChatResponse(reply=error_msg, error_code=ErrorCode.INTENT_NOT_FOUND)
            
            result = await handler.handle(context)
            conversation.add_assistant_message(result.message)
        except Exception as e:
            logger.exception(e)
            conversation.add_assistant_message(str(e))
            return ChatResponse(reply=str(e), error_code=getattr(e, "error_code", ErrorCode.INTERNAL_SERVER_ERROR))

        return ChatResponse(reply=result.message, cart=result.cart, order=result.order)


