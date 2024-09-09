import requests

# API 엔드포인트
endpoint = "https://api.llama.ai/v1/models/3.1-405b/completions"

# API 키 인증
api_key = "LA-96240bd4773f405398ad26c707fbd669ba12ce5cd5664e61a6d520e664d965c9"
headers = {"Authorization": f"Bearer {api_key}"}

# 요청 데이터 준비
data = {"prompt": "Hello, World!"}

# API 호출
response = requests.post(endpoint, headers=headers, json=data)

# 응답 처리
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
