from fastapi import APIRouter
from pydantic import BaseModel


class DronePositionUpdate(BaseModel):
    user_id: str
    string_test: str