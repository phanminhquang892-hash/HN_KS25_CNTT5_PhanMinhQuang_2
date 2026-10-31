from fastapi import FastAPI
from database import Base, engine
from models.models import Device, DeviceType
from routers.routers import router

Base.metadata.create_all(bind=engine)
app = FastAPI(title='Phone Store Management')
app.include_router(router)
