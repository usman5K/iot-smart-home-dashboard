from fastapi import APIRouter

from . import auth, user

routers = APIRouter(prefix="")

routers.include_router(auth.router)
routers.include_router(user.router)
