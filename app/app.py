import streamlit as st
import requests

# URL定義
diary_all_url = "https://simple-diary-app.onrender.com/diarys"
diary_create_url = "https://simple-diary-app.onrender.com/diarys"

url = diary_all_url

if url == diary_all_url:
    response = requests.get(url)
    st.title("日記一覧")
    st.write("---")
    if response.status_code == 200:
        data = response.json()

        st.markdown("""### 新規作成""")

        title = st.text_input("タイトルを入力してください")
        diary_data = st.date_input("日付を選択")
        diary_text = st.text_area("日記の内容")

        if st.button("保存"):

            # 日付を文字列に変換
            diary_data_str = diary_data.strftime('%Y-%m-%d')

            new_diary = {
                "title": title if title else "デフォルトタイトル", 
                "diary_data": diary_data_str,
                "diary_text": diary_text if diary_text else "デフォルト内容",
            }

            # POSTリクエストでデータを送信
            create_response = requests.post(diary_create_url, json=new_diary)

            if create_response.status_code == 201:
                st.success("日記が保存されました！")
            else:
                st.error("日記の保存に失敗しました。")

        if data:
            for diary in data:
                id = diary.get("id", "No id")
                title = diary.get("title", "No title")
                diary_data = diary.get("diary_data", "No data")
                diary_text = diary.get("diary_text", "No diary")
                st.write("---")
                st.write(f"日記番号: {id}")
                st.write(f"タイトル: {title}")
                st.write(f"日付: {diary_data}")
                st.write(f"内容: {diary_text}")
        else:
            st.write("No data found.")
    else:
        st.write("Failed to fetch data from server.")
