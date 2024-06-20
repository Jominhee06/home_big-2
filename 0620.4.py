import random
import requests

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

