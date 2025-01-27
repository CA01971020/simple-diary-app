import streamlit as st
import requests

url = "http://127.0.0.1:8000/datas"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

if data:
    for diary in data:
        id = diary.get("id", "No id")
        title = diary.get("title", "No title")
        diary_data = diary.get("diary_data", "No data")
        diary = diary.get("diary", "No diary")

        st.write(f"日記番号:{id}")
        st.write(f"タイトル:{title}")
        st.write(f"日付:{diary_data}")
        st.write(f"内容:{diary}")

        st.write("---")
else:
    st.write("No data or failed to fetch from server.")