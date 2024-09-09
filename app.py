import os
import streamlit as st
from groq import Groq

# Streamlit 앱 제목 설정
st.title("Groq API를 이용한 챗봇")

# 사이드바에 API 키 입력 필드 추가
GROQ_API_KEY = st.sidebar.text_input("Groq API 키를 입력하세요", type="password")

# 메인 화면에 사용자 입력 필드 추가
user_input = st.text_input("질문을 입력하세요:")

if st.button("답변 받기"):
    if GROQ_API_KEY and user_input:
        try:
            # Groq 클라이언트 초기화
            client = Groq(api_key=GROQ_API_KEY)
            
            # API 호출
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama2-70b-4096",
            )
            
            # 응답 출력
            st.write("답변:", chat_completion.choices[0].message.content)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
    else:
        st.warning("API 키와 질문을 모두 입력해주세요.")
