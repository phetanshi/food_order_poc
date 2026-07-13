from dataclasses import dataclass
from decimal import Decimal

@dataclass
class CartItem:
    food_item_id: int
    food_name: str
    quantity: int
    display_price: Decimal

    @property
    def total_price(self):
        return self.quantity * self.display_price