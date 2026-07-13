from dataclasses import dataclass, field
from decimal import Decimal
from app.domain.cart_item import CartItem

@dataclass
class Cart:
    session_id: str
    items: dict[int, CartItem] = field(default_factory=dict)

    @property
    def is_empty(self):
        return len(self.items) == 0
    
    @property
    def item_count(self):
        return sum(
                    item.quantity 
                    for item in self.items.values()
                   )

