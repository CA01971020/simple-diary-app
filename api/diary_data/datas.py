class Diary:
    def __init__(
        self,
        id:int,
        title:str,
        diary_data:str,
        diary:str,
    ):
        self.id = id
        self.title =title
        self.diary_data = diary_data
        self.diary = diary

diarys = [
    Diary(1,"テスト1","2025年1月27日","テストデータだよ1"),
    Diary(2,"テスト2","2025年1月28日","テストデータだよ2"),
    Diary(3,"テスト3","2025年1月29日","テストデータだよ3")
]

def diarys_all():
    return diarys

def create(diary_create):
    new_diary = Diary(
        len(diarys) + 1,
        diary_create.get("title"),
        diary_create.get("diary_data"),
        diary_create.get("diary"),
    )
    diarys.append(new_diary)
    return(new_diary)