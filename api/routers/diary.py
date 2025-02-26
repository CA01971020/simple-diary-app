from fastapi import APIRouter
from starlette import status
from diary_data import datas as diarys_data
from schemas import DiaryCreate

router = APIRouter(prefix="/diarys",tags=["Diarys"])

@router.get("",status_code=status.HTTP_200_OK)
async def diarys_all():
    return diarys_data.diarys_all()

@router.post("",status_code=status.HTTP_201_CREATED)
async def create(diary_create:DiaryCreate):
    return diarys_data.create(diary_create)