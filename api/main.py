from fastapi import FastAPI
from routers import diary

app = FastAPI()
app.include_router(diary.router)
