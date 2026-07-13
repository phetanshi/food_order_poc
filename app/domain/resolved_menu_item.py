from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class ResolvedMenuItem:
    """
    Domain object returned by MenuResolverService.
    It represents a validated menu item that exists in SQL Server.
    """
    original_name: str
    resolved_name: str
    food_item_id: int
    unit_price: Decimal
    quantity: int