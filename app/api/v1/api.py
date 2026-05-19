from fastapi import APIRouter 
from app.api.v1.endpoint import users,chatbot

api_routes = APIRouter()

api_routes.include_router(users.router,prefix="/users",tags=["users"])
api_routes.include_router(chatbot.router,prefix="/chat",tags=["chat"])