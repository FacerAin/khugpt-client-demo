import logging
import os

import requests
import streamlit as st

logging_dir = "log"
logging_filename = "chat.log"

if not os.path.exists(logging_dir):
    os.makedirs(logging_dir)
logger = logging.getLogger("chat_logger")
logging.basicConfig(filename=os.path.join(logging_dir, logging_filename), level=logging.INFO)
logger.info("Logging from Python module.")


with st.sidebar:
    st.title("KHUGPT")
    st.subheader("이런 내용들을 질문해보세요! 😎")
    st.info("SW 관련 대회 3개 추천해줘")
    st.warning("개발 관련된 취업이나 인턴 정보가 있을까?")
    st.success("내년 대학원 모집 언제부터야?")
    st.error("올해 가을프로그래밍 경시대회 신청 링크 알려줘")
    st.info("인공지능학과 전공 필수 과목 뭐 있어?")
    st.warning("컴퓨터공학과 졸업 요건에 대해 알려줘")
    st.success("SW 관련된 봉사 활동 없을까")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("무엇이 궁금한가요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    logger.info({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.status("찾아보는 중이에요... 🔍잠시만 기다려 주세요! ☺️", expanded=False) as status:
            message_placeholder = st.empty()
            response = requests.post(
                "http://facerain-dev.iptime.org:1009/api/v1/chat/completion",
                json={"query": st.session_state.messages[-1]["content"]},
            )
            answer = response.json()["answer"]
            message_placeholder.markdown(answer)
            status.update(label="찾았어요! 🔥", state="complete", expanded=True)
    st.session_state.messages.append({"role": "agent", "content": response.json()["answer"]})
    logger.info({"role": "agent", "content": response.json()["answer"]})
