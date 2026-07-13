from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Order, FoodItemOrder
from app.domain.cart import Cart
from app.dto import OrderItemDto, OrderResponseDto
from app.exceptions import EmptyCartException, FoodItemNotFoundException
from app.repositories import FoodRepository, OrderRepository


class OrderService:

    def __init__(self, session: AsyncSession, food_repository: FoodRepository, order_repository: OrderRepository):
        self._session = session
        self._food_repository = food_repository
        self._order_repository = order_repository

    async def place_order(self, cart: Cart) -> OrderResponseDto:

        if cart.is_empty:
            raise EmptyCartException(
                "Cart is empty."
            )

        # ------------------------------------------
        # Fetch all food items in ONE query
        # ------------------------------------------

        food_item_ids = [
            item.food_item_id
            for item in cart.items.values()
        ]

        foods = await self._food_repository.get_by_ids(
            food_item_ids
        )

        food_lookup = {
            food.food_item_id: food
            for food in foods
        }

        total = Decimal("0.00")
        order_items: list[OrderItemDto] = []

        try:

            # ------------------------------------------
            # Calculate total
            # ------------------------------------------

            for cart_item in cart.items.values():
                db_food = food_lookup.get(cart_item.food_item_id)

                if db_food is None:
                    raise FoodItemNotFoundException(f"{cart_item.food_name} no longer exists.")

                unit_price = Decimal(
                    str(db_food.food_price)
                )

                line_total = (
                    unit_price *
                    cart_item.quantity
                )

                total += line_total

                order_items.append(
                    OrderItemDto(
                        food_name=db_food.food_item_name,
                        quantity=cart_item.quantity,
                        unit_price=unit_price,
                    )
                )

            # ------------------------------------------
            # Create Order
            # ------------------------------------------

            order = Order(
                order_price=total,
                status="CONFIRMED",
                is_active=True,
            )

            await self._order_repository.create_order(order)
            # Generates OrderId
            await self._session.flush()

            # ------------------------------------------
            # Insert Order Items
            # ------------------------------------------

            order_item_entities = []
            for cart_item in cart.items.values():
                order_item_entities.append(
                    FoodItemOrder(
                        order_id=order.order_id,
                        food_item_id=cart_item.food_item_id,
                        quantity=cart_item.quantity,
                    )
                )

            await self._order_repository.add_order_items(order_item_entities)

            # ------------------------------------------
            # Commit Transaction
            # ------------------------------------------

            await self._session.commit()

            return OrderResponseDto(
                order_id=order.order_id,
                total=total,
                items=order_items,
                message="Your order has been placed successfully."

            )

        except Exception:
            await self._session.rollback()
            raise