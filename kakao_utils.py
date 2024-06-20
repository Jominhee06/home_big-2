import requests
import json

def update_tokens(app_key, filename):
    with open(filename, "r") as f:
        tokens = json.load(f)

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": app_key,
        "refresh_token": tokens['refresh_token']
    }
    response = requests.post(url, data=data)
    tokens.update(response.json())

    with open(filename, "w") as f:
        json.dump(tokens, f)

    return tokens

def send_message(filename, template):
    with open(filename, "r") as f:
        tokens = json.load(f)

    headers = {
        "Authorization": f"Bearer {tokens['access_token']}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "template_object": json.dumps(template)
    }

    url = "	https://kapi.kakao.com/v2/api/talk/memo/send"
    response = requests.post(url, headers=headers, data=data)
    return response
