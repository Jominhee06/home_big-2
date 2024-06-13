import requests

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": "149304769000d8de3ce3a6c7ab50ef48",
    "redirect_uri": "https://localhost.com",
    "code": "rccEZsyCHH0uA1usxvbYauME2WwehotRUNr-HG4nhlC8kdQ0Um2u5QAAAAQKPXTbAAABkA_i-GoSmUam6ZdnFg"
}

response = requests.post(url, data=data)

# 요청에 실패했다면
if response.status_code != 200:
    print("에러 발생! 사유: ", response.json())
else: # 성공했다면
    tokens = response.json()
    print(tokens)
