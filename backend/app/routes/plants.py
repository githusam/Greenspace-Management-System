from fastapi import APIRouter, HTTPException, Security
from app.utils.response import responses
from app.utils.exception import ShapeShyftException
from app.models.garden import GardenEntry
import requests
# create a search endpoint

API_key = "sk-2ONF660f30f1c61564884"

router = APIRouter(
    tags=["plants"],
)

@router.get("/search", responses=responses)
async def search_plant_database(
    query: str
):
    """
    This endpoint searches for plants based on the specific query from an external API
    """
    response = requests.get(url=f"https://perenual.com/api/species-list?key={API_key}&q={query}")
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extracting the required fields from each item in the "data" list
    filtered_data = []
    for item in data["data"]:
        filtered_item = {
            "id": item["id"],
            "common_name": item["common_name"],
        }
        filtered_data.append(filtered_item)
    # Print or do something else with the filtered data
    return filtered_data

@router.get("/watering_details/{id}", responses=responses)
async def get_watering_details(
    id: int
):
    """
    This endpoint searches for plants based on the specific query from an external API
    """
    response = requests.get(url=f"https://perenual.com/api/species/details/{id}?key={API_key}")
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extracting the required fields from each item in the "data" list
    filtered_item = {
        "name": data["common_name"],
        "id": data["id"],
        "frequency": data["watering"], 
        "watering_period": data["watering_period"],
        "times_per_week": data["watering_general_benchmark"]["value"]
    }
    return filtered_item

@router.get("/get_plants_in_garden")
async def get_plants_in_garden():
    entries = await GardenEntry.all()
    return entries

@router.post("/add_to_garden/{id}")
async def add_plant_to_garden(
    id = int
):
    data = await get_watering_details(id)
    plant_to_enter = await GardenEntry.create(name=data["name"], id=data["id"], frequency=data["frequency"], watering_period=data["watering_period"], time_per_week=data["times_per_week"])
    return plant_to_enter

@router.delete("/remove_from_garden/{id}")
async def remove_plant_from_garden(
    id = int
):
    deleted = await GardenEntry.filter(id=id).delete()
    return deleted

@router.get("/plantwatering_schedule/{plant_id}")
async def get_plant_watering_schedule(plant_id: int):
    plant = await GardenEntry.get_or_none(id=plant_id)
    if not plant:
        raise HTTPException(status_code=400, detail="Plant not found")

    time_per_week = plant.time_per_week
    period = plant.watering_period
    
    if period == None:
        period = "N/A"

    if (time_per_week):
        parts = time_per_week.split('-')
        maximum = max([int(part.strip()) for part in parts])

        if maximum == 0:
            return {"dayToWater":[0,0,0,0,0,0,0] ,"periods": [None, None, None, None, None, None, None] }
        if maximum == 1:
            return {"dayToWater":[1,0,0,0,0,0,0] ,"periods": [period, None, None, None, None, None, None] }
        if maximum == 2:
            return {"dayToWater":[1,0,0,1,0,0,0] , "periods": [period, None, None, period, None, None, None] }
        if maximum == 3:
            return {"dayToWater":[1,0,1,0,1,0,0] , "periods": [period, None, period, None, period, None, None] }
        if maximum == 4:
            return {"dayToWater":[1,1,0,1,0,1,0] ,"periods": [period, period, None, period, None, period, None] }
        if maximum == 5:
            return {"dayToWater":[1,1,0,1,1,1,0] ,"periods": [period, period, None, period, period, period, None] }
        if maximum == 6: 
            return {"dayToWater":[1,1,1,0,1,1,1] ,"periods": [period, period, period, None, period, period, period]}
        if maximum == 7:
            return {"dayToWater":[1,1,1,1,1,1,1] ,"periods": [period, period, period, period, period, period, period]}
        if maximum > 7:
            return {"dayToWater":[1,1,1,1,1,1,1],"periods": [period, period, period, period, period, period, period]}
    else:
        return {"dayToWater":[0,0,0,0,0,0,0] ,"periods": [None, None, None, None, None, None, None]}
