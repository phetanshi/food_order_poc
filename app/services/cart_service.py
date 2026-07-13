from decimal import Decimal

from app.domain.cart import Cart
from app.domain.cart_item import CartItem
from app.domain.resolved_menu_item import ResolvedMenuItem
from app.dto import CartItemDto, CartDto


class CartService:
    def __init__(self):
        pass
    
    def calculate_display_total(self, cart: Cart) -> Decimal:
        total = Decimal("0.00")
        for item in cart.items.values():
            total += Decimal(str(item.display_price)) * item.quantity
        return total

    def add_item(self,  cart: Cart, menu_item: ResolvedMenuItem) -> None:
        existing = cart.items.get(menu_item.food_item_id)

        if existing:
            existing.quantity += menu_item.quantity
            return

        cart.items[menu_item.food_item_id] = CartItem(
            food_item_id=menu_item.food_item_id,
            food_name=menu_item.resolved_name,
            quantity=menu_item.quantity,
            display_price=menu_item.unit_price,
        )
    
    def remove_item(self, cart: Cart, menu_item: ResolvedMenuItem, quantity: int = None) -> None:
        existing = cart.items.get(menu_item.food_item_id)

        # Not found in cart, nothing to remove
        if existing is None:
            return

        if quantity is None or quantity >= existing.quantity:
            del cart.items[menu_item.food_item_id]
        else:
            existing.quantity -= quantity
            if existing.quantity <= 0:
                del cart.items[menu_item.food_item_id]
    
    def update_quantity(self, cart: Cart, menu_item: ResolvedMenuItem, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity must be greater than or equal to zero.")

        existing = cart.items.get(menu_item.food_item_id)

        if existing is None:
            raise ValueError("Item not found in cart.")

        if quantity == 0:
            del cart.items[menu_item.food_item_id]
        else:
            existing.quantity = quantity
    
    def clear(self, cart: Cart) -> None:
        cart.items.clear()
    
    def to_dto(self, cart: Cart):
        items = []
        total = Decimal("0.00")

        for item in cart.items.values():
            line_total = Decimal(str(item.display_price)) * item.quantity
            total += line_total
            items.append(
                CartItemDto(
                    food_item_id = item.food_item_id,
                    food_item_name = item.food_name,
                    quantity = item.quantity,
                    unit_price = item.display_price,
                    total_price = line_total
                )
            )

        return CartDto(items=items, total=total)