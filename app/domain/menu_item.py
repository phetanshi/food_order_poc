from dataclasses import dataclass, field
from decimal import Decimal

@dataclass(frozen=True)
class MenuItem:
    food_item_id: int
    name: str
    price: Decimal