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

# 리스트 메시지 URL
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 요청 헤더 설정
headers = {
    "Authorization": "Bearer " + tokens['access_token']
}

# 템플릿 데이터 설정
template = {    
    "object_type": "list",
    "header_title": "로스트아크",
    "header_link": {
        "web_url": "http://www.google.com",
        "mobile_web_url": "http://www.goole.com"
    },
    "contents": [
        {
            "title": "1. 기상술사",
            "description": "기상술사 일러스트",
            "image_url": "https://static.news.zumst.com/images/16/2022/06/25/b71ce41c22d64451ade3db3624170643.jpg",
            "image_width": 50, "image_height": 50,
            "link": {
                "web_url": "http://www.google.com",
                "mobile_web_url": "http://www.google.com"
            }
        },
        {
            "title": "2. 도화가",
            "description": "도화가 일러스트",
            "image_url": "https://dimg.donga.com/wps/NEWS/IMAGE/2022/01/17/111283945.1.jpg",
            "image_width": 50, "image_height": 50,
            "link": {
                "web_url": "http://www.google.com",
                "mobile_web_url": "http://www.google.com"
            }
        }
    ],
    "buttons": [
     {
            "title": "웹으로 이동",
            "link": {
                "web_url": "http://www.google.com",
                "mobile_web_url": "http://www.google.com"
            }
        }
     ]
}
# 데이터를 JSON 형식으로 변환
data = {
    "template_object": json.dumps(template)
}

# 나에게 카카오톡 메시지 보내기 요청 (list)
res = requests.post(url, data=data, headers=headers)
print(res.status_code)

# 요청에 실패했다면,
if res.status_code != 200:
    print("error! because ", res.json())
else: # 성공했다면,
    print('메시지를 성공적으로 보냈습니다.')