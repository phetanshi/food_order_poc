from app.exceptions.food_exception import FoodException


class FoodItemUnavailableException(FoodException):
    """Food exists but is inactive."""