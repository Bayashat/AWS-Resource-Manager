from fastapi import FastAPI

from app.api.s3_routers import router as s3_router

app = FastAPI()

app.include_router(s3_router)
