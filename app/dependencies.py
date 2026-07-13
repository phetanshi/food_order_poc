from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.repositories import FoodRepository, OrderRepository
from app.dispatcher.intent_dispatcher import IntentDispatcher
from functools import lru_cache
from app.services.huggingface_service import HuggingFaceService
from app.services.conversation_service import ConversationManagerService
from app.services.cart_service import CartService
from app.services.menu_resolver_service import MenuResolverService
from app.services.order_service import OrderService
from app.services.chat_service import ChatService


def get_food_repository(db: AsyncSession = Depends(get_db)):
    return FoodRepository(db)


def get_order_repository(db: AsyncSession = Depends(get_db)):
    return OrderRepository(db)

def get_menu_resolver_service(repository: FoodRepository = Depends(get_food_repository)):
    return MenuResolverService(repository)

def get_order_service(db: AsyncSession = Depends(get_db),
                      food_repository: FoodRepository = Depends(get_food_repository),
                      order_repository: OrderRepository = Depends(get_order_repository)):
    return OrderService(db, food_repository, order_repository)


@lru_cache
def get_llm_service() -> HuggingFaceService:
    """
    Singleton instance.
    """
    return HuggingFaceService()

@lru_cache
def get_conversation_manager() -> ConversationManagerService:
    return ConversationManagerService()

@lru_cache
def get_cart_service() -> CartService:
    return CartService()

def get_intent_dispatcher(cart_service: CartService = Depends(get_cart_service),
                           order_service: OrderService = Depends(get_order_service),
                           menu_resolver_service: MenuResolverService = Depends(get_menu_resolver_service)) -> IntentDispatcher:
    return IntentDispatcher(cart_service, order_service, menu_resolver_service)

def get_chat_service(conversation_manager: ConversationManagerService = Depends(get_conversation_manager),
    llm_service: HuggingFaceService = Depends(get_llm_service),
    menu_resolver: MenuResolverService = Depends(get_menu_resolver_service),
    intent_dispatcher: IntentDispatcher = Depends(get_intent_dispatcher)) -> ChatService:
    return ChatService(
        conversation_manager=conversation_manager,
        llm_service=llm_service,
        menu_resolver=menu_resolver,
        intent_dispatcher=intent_dispatcher,
    )