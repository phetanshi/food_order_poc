from app.exceptions.cart_exception import CartException


class CartItemNotFoundException(CartException):
    """Raised when an item does not exist in the cart."""