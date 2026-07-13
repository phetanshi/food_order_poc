from decimal import Decimal
from app.domain.cart import Cart
from app.services.cart_service import CartService


class DummyFoodItem:
    def __init__(self, food_item_id: int, food_item_name: str, food_price: Decimal):
        self.food_item_id = food_item_id
        self.food_item_name = food_item_name
        self.food_price = food_price


def test_add_item():
    cart = Cart("abc")
    service = CartService()
    food_item = DummyFoodItem(food_item_id=1, food_item_name="Pizza", food_price=Decimal("10.50"))

    service.add_item(cart, food_item, quantity=2)

    assert len(cart.items) == 1
    assert 1 in cart.items

    cart_item = cart.items[1]
    assert cart_item.food_item_id == 1
    assert cart_item.food_name == "Pizza"
    assert cart_item.quantity == 2
    assert cart_item.display_price == Decimal("10.50")
