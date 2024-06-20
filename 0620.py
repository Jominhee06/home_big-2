import requests
import json
import datetime
from xml.etree import ElementTree as ET
import random
import kakao_utils

# 기상청 동네예보 조회서비스의 URL
vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

# 기상청 동네예보 조회서비스의 인증키를 입력합니다.
service_key = "omsw2pT9yrE95p9TAi4bhYOAzJlnxj+XZZ47/cpy0kwklITHOCoHDq3K9R8qsSt4rbayma1KptbpmU/WcMFL+A=="

# 기준 날짜와 시간을 설정합니다.
base_date = datetime.datetime.today().strftime("%Y%m%d") #20240620
base_time = "0800"  # 08:00

# 지역 ID를 설정합니다.
nx = "74"
ny = "131"

# 요청할 파라미터를 설정합니다.
params = {
    "serviceKey": service_key,
    "dataType": "json",
    "base_date": base_date,
    "base_time": base_time,
    "nx": nx,
    "ny": ny
}

try:
    # API 요청을 보냅니다.
    res = requests.get(vilage_weather_url, params=params)
    res.raise_for_status()  # HTTP 에러 발생 시 예외 발생

    # JSON 데이터를 파싱합니다.
    result = res.json()

    # API 응답에서 데이터를 추출합니다.
    if result.get('response').get('header').get('resultCode') == '00':
        items = result.get('response').get('body').get('items')
        print(items)
    else:
        error_msg = result.get('response').get('header').get('resultMsg')
        print(f"날씨 정보 요청 실패: {error_msg}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP 에러 발생: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"요청 에러 발생: {req_err}")
except Exception as e:
    print(f"기타 에러 발생: {e}")

# API URL
dust_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

# 기상청 API 서비스 키
service_key = "omsw2pT9yrE95p9TAi4bhYOAzJlnxj+XZZ47/cpy0kwklITHOCoHDq3K9R8qsSt4rbayma1KptbpmU/WcMFL+A=="

# 요청할 파라미터 설정
params = {
    "serviceKey": service_key,
    "returnType": "json",  # JSON 형식으로 응답 받기 위해 설정
    "sidoName": "강원",
    "ver": "1.1"
}

# 요청을 보냅니다.
res = requests.get(dust_url, params=params)

# 응답 상태와 내용을 출력합니다.
print("응답 상태 코드:", res.status_code)
print("응답 내용:", res.text)

# JSON 디코딩을 시도합니다.
dust = dict()  # dust 변수를 미리 정의합니다.
try:
    if res.headers.get('Content-Type').lower().startswith('application/json'):
        result = res.json()
        if res.status_code == 200 and result['response']['header']['resultCode'] == '00':
            dust['PM10'] = {'value': int(result['response']['body']['items'][0]['pm10Value'])}
            dust['PM2.5'] = {'value': int(result['response']['body']['items'][0]['pm25Value'])}
        else:
            print("미세먼지 가져오기 실패: ", result['response']['header']['resultMsg'])
    elif res.headers.get('Content-Type').lower().startswith('application/xml'):
        # XML 응답을 처리합니다.
        root = ET.fromstring(res.text)
        faultstring = root.find('.//faultstring')
        if faultstring is not None:
            print("오류 발생: ", faultstring.text)
        else:
            print("알 수 없는 오류 발생: ", res.text)
    else:
        print("지원하지 않는 응답 형식입니다.")
except json.JSONDecodeError as json_err:
    print("JSON 디코딩 에러 발생: ", json_err)
    print("응답 내용: ", res.text)
except Exception as e:
    print("기타 에러 발생: ", e)

# 결과 출력
print(dust)

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

service_key = "omsw2pT9yrE95p9TAi4bhYOAzJlnxj+XZZ47/cpy0kwklITHOCoHDq3K9R8qsSt4rbayma1KptbpmU/WcMFL+A=="
base_date = datetime.datetime.today().strftime("%Y%m%d")
base_time = "0800"  # 08:00
nx = "74"
ny = "131"

params = {
    "serviceKey": service_key,
    "dataType": "json",
    "base_date": base_date,
    "base_time": base_time,
    "nx" : nx,
    "ny" : ny
}

pty_code = {
    "0": "없음",
    "1": "비",
    "2": "비/눈",
    "3": "눈",
    "4": "소나기",
    "5": "빗방울",
    "6": "빗방울/눈날림",
    "7": "눈날림"
}

data = dict()
data['date'] = base_date
weather = dict()

res = requests.get(vilage_weather_url, params=params)
try:
    result = res.json()
    if 'response' in result and 'body' in result['response'] and 'items' in result['response']['body']:
        items = result['response']['body']['items']
        if 'item' in items:
            for item in items['item']:
                if item['category'] == 'T3H':
                    weather['temperature'] = item['fcstValue']

                if item['category'] == 'PTY':
                    weather['code'] = str(item['fcstValue'])
                    weather['state'] = pty_code.get(str(item['fcstValue']), '알 수 없음')
    else:
        print("날씨 정보를 가져오지 못했습니다.")

except requests.exceptions.RequestException as req_err:
    print(f"요청 에러 발생: {req_err}")
except json.JSONDecodeError as json_err:
    print(f"JSON 디코딩 에러 발생: {json_err}")
except Exception as e:
    print(f"기타 에러 발생: {e}")

data['weather'] = weather
print(data['weather'])

def get_realtime_air_quality(sido_name):
    # API 요청을 보낼 URL
    dust_url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    # 공공데이터포털에서 발급받은 인증키
    service_key = "omsw2pT9yrE95p9TAi4bhYOAzJlnxj+XZZ47/cpy0kwklITHOCoHDq3K9R8qsSt4rbayma1KptbpmU/WcMFL+A=="

    # 요청할 파라미터 설정
    payload = {
        "serviceKey": service_key,
        "returnType": "json",
        "sidoName": sido_name,  # 조회할 시도명
        "ver": "1.0"  # API 버전
    }

    try:
        # API 요청 보내기
        res = requests.get(dust_url, params=payload)
        res.raise_for_status()  # HTTP 요청 오류 확인

        # JSON 형식으로 응답 데이터 파싱
        result = res.json()

        # API 응답에서 실시간 측정 정보 추출
        if result['response']['header']['resultCode'] == '00':
            items = result['response']['body']['items']
            for item in items:
                if item['sidoName'] == sido_name:
                    # 해당 시도의 실시간 측정 정보 출력
                    print(f"{sido_name}의 대기질 측정 정보:")
                    print(f"- 측정소명: {item['stationName']}")
                    
                    # 미세먼지(PM10) 처리
                    if item['pm10Value'] != '-':
                        print(f"- 미세먼지(PM10): {item['pm10Value']} ㎍/m³, 상태:{get_pm_state(int(item['pm10Value']), 'PM10')}")
                    else:
                        print("- 미세먼지(PM10): 측정값 없음")
                    
                    # 초미세먼지(PM2.5) 처리
                    if item['pm25Value'] != '-':
                        print(f"- 초미세먼지(PM2.5): {item['pm25Value']} ㎍/m³, 상태:{get_pm_state(int(item['pm25Value']), 'PM2.5')}")
                    else:
                        print("- 초미세먼지(PM2.5): 측정값 없음")
                    
                    print()  # 개행을 통해 정보 간 구분
        else:
            error_msg = result['response']['header']['resultMsg']
            print(f"API 요청 실패: {error_msg}")

    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")

# PM 상태 판별 함수
def get_pm_state(pm_value, pm_type):
    if pm_value < 0:
        return "알 수 없음"
    elif pm_type == 'PM10':
        if pm_value < 30:
            return "좋음"
        elif pm_value < 80:
            return "보통"
        elif pm_value < 150:
            return "나쁨"
        else:
            return "매우 나쁨"
    elif pm_type == 'PM2.5':
        if pm_value < 15:
            return "좋음"
        elif pm_value < 35:
            return "보통"
        elif pm_value < 75:
            return "나쁨"
        else:
            return "매우 나쁨"

# 실행 코드
if __name__ == "__main__":
    sido_name = "강원"  # 조회할 시도명 설정 (예: 서울, 부산, 인천 등)
    get_realtime_air_quality(sido_name)

    rain_foods = "부대찌개,아구찜,해물탕,칼국수,수제비,짬뽕,우동,치킨,국밥,김치부침개,두부김치,파전".split(',')
pmhigh_foods = "콩나물국밥,고등어,굴,쌀국수,마라탕".split(',')

def get_foods_list(weather, dust_pm10, dust_pm25):
    if weather != '0':
        recommand_state = 'Case1'
        foods_list = random.sample(rain_foods, k=3)  # 비오는 날 음식 3개 추천
    elif dust_pm10 == '매우나쁨' or dust_pm25 == '매우나쁨':
        recommand_state = 'Case2'
        foods_list = random.sample(pmhigh_foods, k=3)  # 미세먼지 상태가 나쁜 경우 음식 3개 추천
    else:
        recommand_state = 'Case3'
        foods_list = []  # 정상적인 경우 빈 리스트 반환
    
    return recommand_state, foods_list

def naver_local_search(query, display):
    headers = {
        "x-Naver-Client-Id": "2ol9QKDvtdeLIlHpm0bP",
        "x-Naver-Client-Secret": "jbHTeYkQsU"
    }
    params = {
        "sort": "comment",
        "query": query,
        "display": display
    }
    naver_local_url = "https://openapi.naver.com/v1/search/local.json"
    try:
        res = requests.get(naver_local_url, headers=headers, params=params)
        res.raise_for_status()  # HTTP 요청 오류 확인
        places = res.json().get('items')
        return places
    except requests.exceptions.RequestException as e:
        print(f"네이버 API 요청 중 오류 발생: {e}")
        return []

# 가상의 데이터로 대체
data = {
    'weather': {'code': '1'},
    'dust': {'PM10': {'state': '보통'}, 'PM2.5': {'state': '보통'}}
}

try:
    weather = data.get('weather').get('code')
    dust_pm10 = data.get('dust').get('PM10').get("state")
    dust_pm25 = data.get('dust').get('PM2.5').get("state")
except AttributeError as e:
    print(f"데이터 접근 중 오류 발생: {e}")
    weather = '0'
    dust_pm10 = '보통'
    dust_pm25 = '보통'

weather_state, foods_list = get_foods_list(weather, dust_pm10, dust_pm25)
location = "원주"

recommands = []

for food in foods_list:
    query = location + " " + food + " 맛집"
    result_list = naver_local_search(query, 3)

    if result_list is not None and len(result_list) > 0:
        if weather_state == 'Case3':
            recommands = result_list
            break
        else:
            recommands.append(result_list[0])
    else:
        print(f"검색 결과 없음: {query}")

if recommands:
    print("비오는 날 추천 음식:")
    for idx, place in enumerate(recommands, start=1):
        print(f"{idx}. {place['title']} - {place['roadAddress'] if 'roadAddress' in place else place['address']}")
else:
    print("음식 추천 결과가 없습니다.")


KAKAO_TOKEN_FILENAME = "D:\Joo.min.hee\IOT강의\Source.1\kakao_message\kakao_token.json"
KAKAO_APP_KEY = "053d9f9c75df468f95503ff47c53f78c"
TEMPLATE_ID = "3588274176"  # 카카오 디벨로퍼스에서 생성한 템플릿 ID로 대체


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