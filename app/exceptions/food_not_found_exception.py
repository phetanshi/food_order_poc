from app.exceptions.food_exception import FoodException


class FoodItemNotFoundException(FoodException):
    """Food item not found in database."""