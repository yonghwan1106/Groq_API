import streamlit as st
import requests

# API 엔드포인트
endpoint = "https://api.llama.ai/v1/models/70b" 

# API 키 인증
api_key = "LA-372b2dec00874a9b8197263d16aeeef317465303cac244888ac2e2175cc5b458"  # YOUR_API_KEY를 실제 API 키로 대체하세요.

# Streamlit 앱 생성
st.title("LLaMA API 테스트")

# 사용자 입력 받기
prompt = st.text_input("prompt를 입력하세요.")

endpoint = "https://api.llama.ai/v1/models/70b"
api_key = "LA-372b2dec00874a9b8197263d16aeeef317465303cac244888ac2e2175cc5b458"

headers = {"Authorization": f"Bearer {api_key}"}
data = {"prompt": "Hello, World!"}

response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
