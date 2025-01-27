from fastapi import FastAPI
from diary_data import datas as diarys_date

app = FastAPI()

@app.get("/datas")
async def diarys_all():
    return diarys_date.diarys_all()