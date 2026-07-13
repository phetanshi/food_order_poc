from app.dto import Intent
from app.services.cart_service import CartService
from app.services.handlers.end_conversation_intent_handler import EndConversationHandler
from app.services.order_service import OrderService
from app.services.menu_resolver_service import MenuResolverService

from app.services.handlers import (
    AddItemHandler, 
    RemoveItemHandler, 
    UpdateQuantityHandler, 
    ShowCartHandler, 
    ShowTotalHandler, 
    ConfirmOrderHandler, 
    CancelOrderHandler, 
    ShowMenuHandler, 
    GreetingHandler
)


class IntentDispatcher:

    def __init__(self, cart_service: CartService, order_service: OrderService, menu_resolver_service: MenuResolverService):
        self.handlers = {
            Intent.GREETING: GreetingHandler(menu_resolver_service),
            Intent.ADD_ITEM: AddItemHandler(cart_service, menu_resolver_service),
            Intent.REMOVE_ITEM: RemoveItemHandler(cart_service, menu_resolver_service),
            Intent.UPDATE_QUANTITY: UpdateQuantityHandler(cart_service, menu_resolver_service),
            Intent.SHOW_CART: ShowCartHandler(cart_service),
            Intent.SHOW_TOTAL: ShowTotalHandler(cart_service),
            Intent.CONFIRM_ORDER: ConfirmOrderHandler(cart_service, order_service),
            Intent.CANCEL_ORDER: CancelOrderHandler(cart_service),
            Intent.SHOW_MENU: ShowMenuHandler(menu_resolver_service),
            Intent.END_CONVERSATION: EndConversationHandler()
        }

    def get_handler(self, intent):
        return self.handlers[intent]