from fastapi import APIRouter, HTTPException, Security
import requests
from app.utils.response import responses

apikey=""

router=APIRouter(
    tags=["Plants"],
)

@router.get("/")
async def search(query: str):
    api_url= f"https://perenual.com/api/species-list?key={apikey}&q={query}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from API")
