from fastapi import APIRouter, HTTPException
from app.api.utils.sensors import *
from app.api.schemas.sensors import *

sensors_router = APIRouter(tags=["Sensors"], prefix="/api")


@sensors_router.get("/sensors/data")
def get_sensors_data():
    response = ""
    return response
