from app.exceptions.order_exception import OrderException


class OrderCreationException(OrderException):
    """Order could not be created."""