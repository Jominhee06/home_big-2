import requests

# 접속 데이터 추가 예제
def add_activity(user_id, login_time, logout_time):
    url = 'https://www.gametrics.com/gameindex/GameIndex_Main.aspx'
    payload = {
        'user_id': user_id,
        'login_time': login_time,
        'logout_time': logout_time
    }
    response = requests.post(url, json=payload)
    return response.json()

# 접속률 조회 예제
def get_activity_rate(start_time, end_time):
    url = 'https://www.gametrics.com/gameindex/GameIndex02.aspx'
    params = {
        'start_time': start_time,
        'end_time': end_time
    }
    response = requests.get(url, params=params)
    return response.json()

# 테스트 데이터 추가
add_activity('user1', '2024-06-19 10:00:00', '2024-06-19 11:00:00')
add_activity('user2', '2024-06-19 10:30:00', '2024-06-19 11:30:00')

# 접속률 조회
rate = get_activity_rate('2024-06-19 10:00:00', '2024-06-19 12:00:00')
print(rate)
