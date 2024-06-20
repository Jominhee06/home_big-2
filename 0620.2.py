import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

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
