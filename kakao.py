import requests
import json

def send_kakao_message(token_filename, template_id, data):
    # 토큰 파일에서 액세스 토큰 읽어오기
    with open(token_filename, 'r') as f:
        tokens = json.load(f)
        access_token = tokens['access_token']

    # 카카오 메시지 API 호출을 위한 URL
    kakao_message_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 메시지 헤더 설정
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # 메시지 내용 설정
    payload = {
        "template_id": template_id,  # 사용할 템플릿 ID
        "template_args": json.dumps(data)  # 템플릿에 전달할 데이터
    }

    try:
        # 카카오 메시지 API 호출
        res = requests.post(kakao_message_url, headers=headers, data=payload)
        res.raise_for_status()  # HTTP 요청 오류 확인
        
        # 성공적으로 메시지 전송한 경우
        if res.json().get('result_code') == 0:
            print('카카오 메시지 전송 성공')
        else:
            print('카카오 메시지 전송 실패:', res.json())
    
    except requests.exceptions.RequestException as e:
        print(f"카카오 메시지 API 호출 중 오류 발생: {e}")

# 실행 예제
if __name__ == "__main__":
    KAKAO_TOKEN_FILENAME = "D:\Joo.min.hee\IOT강의\Source.1\kakao_message\kakao_token.json"
    TEMPLATE_ID = "3588274176"  # 사용할 템플릿 ID 입력
    message_data = {
        "data": "날씨 정보",
        "weather": {
            "tmp": "24",
            "dust": {
                "PM10": {
                    "value": "30",
                    "state": "보통"
                },
                "PM2.5": {
                    "value": "15",
                    "state": "좋음"
                }
            }
        }
    }

    send_kakao_message(KAKAO_TOKEN_FILENAME, TEMPLATE_ID, message_data)
