from fastapi import FastAPI,Body
from diary_data import datas as diarys_data

app = FastAPI()

@app.get("/datas")
async def diarys_all():
    return diarys_data.diarys_all()

@app.post("/create")
async def create(diary_create=Body()):
    return diarys_data.create(diary_create)