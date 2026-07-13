from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DECIMAL,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class FoodItem(Base):

    __tablename__ = "FoodItems"

    food_item_id: Mapped[int] = mapped_column(
        "FoodItemId",
        Integer,
        primary_key=True
    )

    food_item_name: Mapped[str] = mapped_column(
        "FoodItemName",
        String(100),
        nullable=False,
        unique=True
    )

    food_price: Mapped[float] = mapped_column(
        "FoodPrice",
        DECIMAL(10, 2),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        default=True
    )

    orders = relationship(
        "FoodItemOrder",
        back_populates="food_item"
    )

class Order(Base):

    __tablename__ = "Orders"

    order_id: Mapped[int] = mapped_column(
        "OrderId",
        Integer,
        primary_key=True
    )

    order_price: Mapped[float] = mapped_column(
        "OrderPrice",
        DECIMAL(10, 2)
    )

    status: Mapped[str] = mapped_column(
        "Status",
        String(30)
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        default=True
    )

    food_items = relationship(
        "FoodItemOrder",
        back_populates="order"
    )

class FoodItemOrder(Base):

    __tablename__ = "FoodItemOrder"

    food_item_order_id: Mapped[int] = mapped_column(
        "FoodItemOrderId",
        Integer,
        primary_key=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("Orders.OrderId")
    )

    food_item_id: Mapped[int] = mapped_column(
        ForeignKey("FoodItems.FoodItemId")
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )

    order = relationship(
        "Order",
        back_populates="food_items"
    )

    food_item = relationship(
        "FoodItem",
        back_populates="orders"
    )