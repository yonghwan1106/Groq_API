import streamlit as st
import requests
import json

# Streamlit 앱 제목 설정
st.title("Groq API를 이용한 챗봇")

# 세션 상태 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Groq API 키를 secrets에서 가져오기
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# 사이드바에 모델 선택 옵션 추가
MODEL = st.sidebar.selectbox(
    "사용할 모델을 선택하세요",
    ("llama-3.1-70b-versatile", "llama3-70b-8192", "llama3-8b-8192", "whisper-large-v3")
)

# 채팅 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
def process_input():
    if user_input := st.chat_input("질문을 입력하세요:"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
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
                "messages": st.session_state.messages
            }
            
            # API 요청 보내기
            response = requests.post(url, headers=headers, data=json.dumps(data))
            
            # 응답 처리
            if response.status_code == 200:
                result = response.json()
                assistant_response = result['choices'][0]['message']['content']
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)
            else:
                st.error(f"API 오류: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")

# 사용자 입력 처리 함수 호출
process_input()
