from schemas import DiaryCreate

class Diary:
    def __init__(
        self,
        id:int,
        title:str,
        diary_data:str,
        diary_text:str,
    ):
        self.id = id
        self.title =title
        self.diary_data = diary_data
        self.diary_text = diary_text

diarys = [
    Diary(1,"テスト","2025年1月27日","テストデータ"),
]

def diarys_all():
    return diarys

def create(diary_create:DiaryCreate):
    new_diary = Diary(
        len(diarys) + 1,
        diary_create.title,
        diary_create.diary_data,
        diary_create.diary_text
    )
    diarys.append(new_diary)
    return(new_diary)