import streamlit as st
import requests
import json

# Streamlit 앱 제목 설정
st.title("Groq API를 이용한 챗봇")

# 사이드바에 API 키 입력 필드 추가
GROQ_API_KEY = st.sidebar.text_input("Groq API 키를 입력하세요", type="password")

# 사이드바에 모델 선택 옵션 추가
MODEL = st.sidebar.selectbox(
    "사용할 모델을 선택하세요",
    ("llama3-70b-8192", "llama-3.1-70b-versatile", "llama3-8b-8192", "whisper-large-v3")
)

# 메인 화면에 사용자 입력 필드 추가
user_input = st.text_input("질문을 입력하세요:")

if st.button("답변 받기"):
    if GROQ_API_KEY and user_input:
        try:
            # API 요청 URL
            url = "https://api.groq.com/openai/v1/chat/completions"
            
            # 요청 헤더
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # 요청 본문
            data = {
                "model": MODEL,
                "messages": [{"role": "user", "content": user_input}]
            }
            
            # API 요청 보내기
            response = requests.post(url, headers=headers, data=json.dumps(data))
            
            # 응답 처리
            if response.status_code == 200:
                result = response.json()
                st.write("답변:", result['choices'][0]['message']['content'])
            else:
                st.error(f"API 오류: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
    else:
        st.warning("API 키와 질문을 모두 입력해주세요.")
