from app.exceptions.cart_exception import CartException


class EmptyCartException(CartException):
    """Raised when attempting to checkout an empty cart."""