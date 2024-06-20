import requests

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
        "ver": "1.0"  # API 버전 (1.1 대신 1.0으로 수정)
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
                        print(f"- 미세먼지(PM10): {item['pm10Value']} ㎍/m³, 상태: {get_pm_state(int(item['pm10Value']), 'PM10')}")
                    else:
                        print("- 미세먼지(PM10): 측정값 없음")
                    
                    # 초미세먼지(PM2.5) 처리
                    if item['pm25Value'] != '-':
                        print(f"- 초미세먼지(PM2.5): {item['pm25Value']} ㎍/m³, 상태: {get_pm_state(int(item['pm25Value']), 'PM2.5')}")
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


