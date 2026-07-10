from fastapi import FastAPI

from app.api.customers import router as customer_router
from app.api.health import router as health_router
from app.db.base import Base
from app.db.database import engine

# Import all models
from app.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopSphere Source System",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(customer_router)