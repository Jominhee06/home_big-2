import json
import kakao_utils

KAKAO_TOKEN_FILENAME = "D:/Joo.min.hee/프로그래밍기초/kakao_message/kakao_token.json"
KAKAO_APP_KEY = "053d9f9c75df468f95503ff47c53f78c"

# 토큰 업데이트
kakao_utils.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)

# 가상의 데이터로 대체
data = {
    'weather': {'tmp': '25도'},
    'dust': {'PM10': {'value': '30', 'state': '보통'}, 'PM2.5': {'value': '15', 'state': '좋음'}}
}

weather_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%82%A0%EC%94%A8&oquery=%EB%82%A0&tqi=iFngbdpzLi0sslrf89Nssssst5l-318826"

text = f"""\
# 날씨 정보
기온 : {data['weather']['tmp']}
미세먼지 : {data['dust']['PM10']['value']}, {data['dust']['PM10']['state']}
초미세먼지 : {data['dust']['PM2.5']['value']}, {data['dust']['PM2.5']['state']}
"""

template = {
    "object_type": "text",
    "text": text,
    "link": {
        "web_url": weather_url,
        "mobile_web_url": weather_url
    },
    "button_title": "날씨 상세보기"
}

res = kakao_utils.send_message(KAKAO_TOKEN_FILENAME, template)
if res.json().get('result_code') == 0:
    print('날씨 및 미세먼지 정보 성공적으로 보냈습니다.')
else:
    print('날씨 및 미세먼지 정보를 성공적으로 보내지 못했습니다. 오류메세지 : ', res.json())
