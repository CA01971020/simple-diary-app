import streamlit as st
import requests

# URL定義
url = ""
diary_all_url ="http://127.0.0.1:8000/datas"
diary_create_url ="http://127.0.0.1:8000/create"

if st.button("日記一覧"):
    url = diary_all_url

if st.button("新規作成"):
    url = diary_create_url

st.write("---")

# 日記一覧表示
if url == diary_all_url:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data:
            for diary in data:
                id = diary.get("id", "No id")
                title = diary.get("title", "No title")
                diary_data = diary.get("diary_data", "No data")
                diary_text = diary.get("diary", "No diary")

                st.write(f"日記番号: {id}")
                st.write(f"タイトル: {title}")
                st.write(f"日付: {diary_data}")
                st.write(f"内容: {diary_text}")
                st.write("---")
        else:
            st.write("No data found.")
    else:
        st.write("Failed to fetch data from server.")

# 新規作成表示
elif url == diary_create_url:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data:
                st.write("test")
        else:
            st.write("No data found.")
    else:
        st.write("Failed to fetch data from server.")
else:
    st.write("Please select an action.")
