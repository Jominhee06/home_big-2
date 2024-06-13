import requests

url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization": "KakaoAK 149304769000d8de3ce3a6c7ab50ef48"
}
params = {
    "query": "도화가"
}

# 이미지 검색 요청
response = requests.get(url, headers=headers, params=params)

# 요청에 실패했다면
if response.status_code != 200:
    print("Error! Status Code:", response.status_code)
    print("Response:", response.json())
else:  # 성공했다면
    count = 0
    images = response.json().get('documents', [])
    if not images:
        print("No images found for the query.")
    else:
        for image_info in images:
            print(f"[{count}th] image_url =", image_info['image_url'])
            count += 1
            if count >= 10:  # 제한된 수의 이미지 URL을 출력
                break
