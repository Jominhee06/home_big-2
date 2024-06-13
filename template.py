import json
import requests

# 토큰 정보를 파일에서 불러오는 함수 정의
def load_tokens(filename):
    with open(filename, 'r', encoding='utf-8') as file:
      tokens = json.load(file)
    return tokens

# 토큰이 저장된 파일 경로
KAKAO_TOKEN_FILENAME = 'D:\Joo.min.hee\IOT강의\Source.1\kakao_message\kakao_token.json'

# 저장된 토큰 정보 불러오기
tokens = load_tokens(KAKAO_TOKEN_FILENAME)

# 텍스트 메시지 URL
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 액세스 토큰을 포함한 요청 헤더 설정
headers = {
    "Authorization": "Bearer " + tokens['access_token']
}
# 요청에 보낼 데이터 설정
data = {
    "template_object": json.dumps({
        "object_type": "text",
        "text": "Hello, world!",
        "link": {
            "web_url": "http://www.google.com"
        }
    })
}
# 카카오톡 메시지 보내기 요청
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# 요청이 성공했는지 확인
if response.status_code != 200:
    print("error! because ", response.json())
else:
    print('메시지를 성공적으로 보냈습니다.')
