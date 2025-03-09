from fastapi import APIRouter, HTTPException
import requests
from app.api.utils.drones import *
from app.api.schemas.drones import *
from app.core.websockets import ConnectionManager

drones_router = APIRouter(tags=["Drones"], prefix="/api")
connection_manager = ConnectionManager()


@drones_router.get("/drone/position")
def get_drone_position():
    response = ""
    return response


@drones_router.put("/drone/position")
async def update_drone_position(data: DronePositionUpdate):
    response = ""
    await connection_manager.broadcast_message(data.user_id, data.string_test)
    return response
