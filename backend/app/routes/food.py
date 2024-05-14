from fastapi import APIRouter, HTTPException, Security
from app.utils.response import responses
from app.utils.exception import ShapeShyftException
from fatsecret import Fatsecret

fs = Fatsecret("0047da412ebd469c9dd1895c7d3159d8", "2f91d6bcbaa94e72bea327eb4d6b0546")
# create a search endpoint

router = APIRouter(
    tags=["Food & Calories"],
)

@router.get("/search", responses=responses)
async def search_food_database(
    query: str
):
    """
    This endpoint searches for food items based on the query string
    """
    foods = fs.foods_search(query)
    foods_array = []
    return foods
