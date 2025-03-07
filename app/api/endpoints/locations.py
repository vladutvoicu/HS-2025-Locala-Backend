from fastapi import APIRouter, HTTPException
from app.api.utils.locations import *
from app.api.schemas.locations import *

locations_router = APIRouter(tags=["Locations"], prefix="/api")


@locations_router.get("/locations")
def get_locations():
    response = ""
    return response


@locations_router.post("/locations")
def post_locations():
    response = ""
    return response