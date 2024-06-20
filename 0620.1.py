import requests
import json
import datetime
from xml.etree import ElementTree as ET

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




