import streamlit as st
import requests

# API 키를 코드에 직접 입력
api_key = "LA-372b2dec00874a9b8197263d16aeeef317465303cac244888ac2e2175cc5b458"

# Streamlit 앱 생성
st.title("LLaMA API 테스트")

# 사용자 입력 받기
prompt = st.text_input("prompt를 입력하세요.")

def send_api_request(prompt):
    endpoint = "https://api.llama.ai/v1/models/70b/generate"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"prompt": prompt}
    response = requests.post(endpoint, headers=headers, json=data)
    return response

def handle_response(response):
    if response.status_code == 200:
        result = response.json()
        st.write(result)
    else:
        st.write(f"Error: {response.status_code} - {response.text}")

if st.button("API 요청 보내기"):
    response = send_api_request(prompt)
    handle_response(response)
