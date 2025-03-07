from fastapi import APIRouter, HTTPException
from app.api.utils.routes import *
from app.api.schemas.routes import *

routes_router = APIRouter(tags=["Routes"], prefix="/api")


@routes_router.get("/route/optimal")
def get_optimal_route():
    response = ""
    return response