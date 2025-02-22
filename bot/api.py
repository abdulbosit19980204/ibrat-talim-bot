from urllib import response

import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1/'


def create_user(username, user_id, name, surname):
    url = f'{BASE_URL}users/'
    data = {
        "username": username,
        "user_id": user_id,
        "name": name,
        "surname": surname,
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url=url, json=data, headers=headers)

    # print(response.status_code, response.json())  # Javobni tekshirish
    return response.json()


# create_user("user3", 3, 'userbot3')


def get_users():
    url = f'{BASE_URL}users/'
    response = requests.get(url=url)
    # print(response.status_code, response.json())
    return response.json()


# get_users()

def create_feedback(user_id, body):
    url = f'{BASE_URL}feedbacks/'
    data = {
        "user_id": user_id,
        "body": body
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, json=data, headers=headers)
    # print(response.status_code, response.json())
    return response.json()


# create_feedback(1, "Assalomu alaykum bot ishga tushdi")

def get_filiallar():
    d = {}
    url = f'{BASE_URL}filiallar/'
    response = requests.get(url=url).json()
    for j in response:
        d[j["name"]] = j['filial_detail']
    return d


def get_yonalishlar():
    d = {}
    url = f'{BASE_URL}yonalishlar/'
    response = requests.get(url=url).json()
    return response
