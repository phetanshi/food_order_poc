from app.exceptions.cart_exception import CartException


class InvalidQuantityException(CartException):
    """Raised when quantity is invalid."""