import requests
import streamlit as st

st.title("KHUGPT Demo v0.1")

query = st.text_input("질문을 입력해주세요.")
run = st.button("실행")
if run:
    data = {"query": query}
    response = requests.post("http://localhost:8000/api/v1/chat/completion", json=data)
    st.warning(response.json()["answer"])
