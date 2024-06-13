import json
import requests
import datetime
import os

# 카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "D:\Joo.min.hee\IOT강의\Source.1\kakao_message\kakao_token.json"

# 디렉토리가 없으면 생성하는 함수
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# 토큰을 저장하는 함수
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

# 토큰을 읽어오는 함수
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens

# refresh_token으로 access_token 갱신하는 함수
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": app_key,
        "refresh_token": tokens['refresh_token']
    }
    response = requests.post(url, data=data)

    # 요청에 실패한 경우,
    if response.status_code != 200:
        print("에러 발생! 사유: ", response.json())
        tokens = None
    else: # 요청에 성공한 경우,
        print(response.json())
        # 기존 파일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename + "." + now
        os.rename(filename, backup_filename)
        # 갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
        
    return tokens

# 디렉토리 생성
ensure_dir(os.path.dirname(KAKAO_TOKEN_FILENAME))

# 예시 토큰 데이터 (실제로는 유효한 토큰 데이터를 여기에 할당해야 함)
tokens = {
    "access_token": "TRMZRysNRritWw1duZ5Mp8O6-uW3XXYoAAAAAQo9c-wAAAGQD-bvBOiSikwhugC4",
    "refresh_token": "TVN4vfzeG690Vs7ZIOVf8tLz6QhzHoZfAAAAAgo9c-wAAAGQD-bvAeiSikwhugC4"
}

# 토큰 저장
save_tokens(KAKAO_TOKEN_FILENAME, tokens)

# 토큰 업데이트 -> 토큰 저장 필수!
# KAKAO_APP_KEY = "<REST_API 앱키를 입력하세요>"
# tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
# save_tokens(KAKAO_TOKEN_FILENAME, tokens)
