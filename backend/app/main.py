from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routers import routers
from backend.app.utils.database import Base, engine
from backend.app.utils.settings import logger

app = FastAPI(
    title="IoT Smart Home API",
    description="API collection for IoT Smart Home Project",
    version="0.1"
)

@app.on_event("startup")
def on_startup():
    logger.info("Creating tables")
    Base.metadata.create_all(engine)


app.add_middleware(
    CORSMiddleware, # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Smart Home Dashboard API"}


app.include_router(routers)
