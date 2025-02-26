from typing import Optional
from pydantic import BaseModel,Field

class DiaryCreate(BaseModel):
    title:str  = Field(min_length=1,max_length=20,examples=["タイトル"])
    diary_data:str = Field(examples=["XXXX年X月XX日"])
    diary_text:Optional[str] = Field(None,examples=["キョウのデキゴト"])