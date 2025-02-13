# プロジェクトセットアップ方法

## 環境構築

### requirements.txt

```txt
fastapi
uvicorn
streamlit
requests
pydantic
```

### インストール

プロジェクトのディレクトリで以下を実行

```
pip install -r requirements.txt
```

### streamlit 起動

```
cd app
```

```
streamlit run app.py
```

### FastAPI 仮想環境起動

```
cd api
```

```
.\env\Scripts\activate
```

```
uvicorn main:app --reload
```

## フォルダ構成
