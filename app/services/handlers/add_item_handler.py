from app.dto import ChatResult
from app.services.cart_service import CartService
from app.services.handlers.base_handler import BaseIntentHandler
from app.services.handlers.handler_context import HandlerContext
from app.services.menu_resolver_service import MenuResolverService


class AddItemHandler(BaseIntentHandler):

    def __init__(self, cart_service: CartService, menu_resolver: MenuResolverService):
        self.cart_service = cart_service
        self.menu_resolver = menu_resolver

    async def handle(self, context: HandlerContext) -> ChatResult:
        resolved_items, unavailable = await self.menu_resolver.resolve_entities(context.llm_response)

        # -------------------------------------------------------
        # Some requested items are unavailable
        # -------------------------------------------------------

        if unavailable:
            menu = await self.menu_resolver.get_menu()

            def _fmt_item(item):
                name = getattr(item, "food_item_name", None) \
                    or getattr(item, "FoodItemName", None) \
                    or getattr(item, "name", str(item))

                price = getattr(item, "food_price", None) \
                    or getattr(item, "FoodPrice", None)

                try:
                    price_text = (
                        f" (₹{float(price):.2f})"
                        if price is not None else ""
                    )
                except Exception:
                    price_text = (
                        f" ({price})"
                        if price is not None else ""
                    )

                return f"{name}{price_text}"

            available_items = (
                ", ".join(_fmt_item(item) for item in menu)
                if menu
                else "No items available"
            )

            return ChatResult(
                message=(
                    f"Sorry, we don't serve "
                    f"{', '.join(unavailable)}.\n\n"
                    f"Available menu:\n{available_items}"
                )
            )

        # -------------------------------------------------------
        # Add all resolved items to cart
        # -------------------------------------------------------

        for menu_item in resolved_items:
            self.cart_service.add_item(
                cart=context.conversation.cart,
                menu_item=menu_item,
            )

        cart = self.cart_service.to_dto(context.conversation.cart)

        return ChatResult(message="Items added successfully.",cart=cart)