from app.api.routers import user, appointment
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(appointment.router)
