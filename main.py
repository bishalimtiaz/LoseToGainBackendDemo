# super admin : super1507!@#$

from fastapi import FastAPI
from mobile.api.api_v1 import mobile_api
from web.api.api_v1 import web_api

from models import meta
from security.database import engine

meta.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(web_api.api_router)
app.include_router(mobile_api.api_router)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
