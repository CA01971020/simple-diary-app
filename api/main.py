from fastapi import FastAPI
from api.routers import diary

app = FastAPI()
app.include_router(diary.router)
