from fastapi import APIRouter, HTTPException
from app.api.utils.drones import *
from app.api.schemas.drones import *

drones_router = APIRouter(tags=["Drones"], prefix="/api")


@drones_router.get("/drone/position")
def get_drone_position():
    response = ""
    return response


@drones_router.put("/drone/position")
def update_drone_position():
    response = ""
    return response