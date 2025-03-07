from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.locations import locations_router
from app.api.endpoints.routes import routes_router
from app.api.endpoints.drones import drones_router
from app.api.endpoints.sensors import sensors_router

router = FastAPI()

router.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.include_router(locations_router)
router.include_router(routes_router)
router.include_router(drones_router)
router.include_router(sensors_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(router, host="0.0.0.0", port=8000)
