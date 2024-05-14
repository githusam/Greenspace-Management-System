from pydantic import UUID4, BaseModel, EmailStr, validator, Field


from .general import Response

from tortoise.contrib.pydantic import pydantic_model_creator
from decimal import Decimal
class Food(BaseModel):
    name: str
    unit: str
    calories: str
    fat: str
    carbs: str
    protein: str
    link: str
    number_of_units: int = 1

class FoodSearchResponse(Response):
    items: list[Food]

class MealRecommendationResponse(Response):
    breakfast: str
    lunch: str
    dinner: str
    snack: str
    calories: str

class MealPlan(BaseModel):
    breakfast: str
    lunch: str
    dinner: str
    snack: str
    calories: str

class TotalCaloriesResponse(Response):
    total_calories: Decimal

class PredictCaloriesRequest(BaseModel):
    weight: float
    height: float
    age: int

class CaloriePredictionResponse(Response):
    calories: float

