from urllib import response

import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1/'


def create_user(username, user_id, name, surname, phone_number):
    url = f'{BASE_URL}users/'
    data = {
        "username": username,
        "user_id": user_id,
        "name": name,
        "surname": surname,
        "phone_number": phone_number,
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


def update_user_phone(user_id, phone_number):
    users = get_users()
    for user in users:
        if str(user['user_id']) == str(user_id):
            url = f'{BASE_URL}users/{user['id']}/'
            user['phone_number'] = phone_number
            response = requests.put(url=url, json=user)
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


def get_price():
    url = f'{BASE_URL}prices/'
    response = requests.get(url=url).json()
    return response


def get_chegirma():
    d = {}
    url = f'{BASE_URL}chegirmalar/'
    response = requests.get(url=url).json()
    return response


def format_chegirmalar(chegirmalar):
    text = "🎁 <b>Bizning maxsus chegirmalar!</b>\n\n"

    for chegirma in chegirmalar:
        chegirma_miqdori = ""
        if chegirma["is_foiz"]:
            chegirma_miqdori = f"<b>{chegirma['miqdori']}%</b> chegirma"
        elif chegirma["is_miqdor"]:
            chegirma_miqdori = f"<b>{int(chegirma['miqdori']):,} UZS</b> chegirma".replace(",", " ")

        fanlar_text = ", ".join([fan["name"] for fan in chegirma["fan"]])

        text += f"🔹 <b>{chegirma['name']}</b>\n"
        text += f"📚 <b>Fanlar:</b> {fanlar_text}\n"
        text += f"💰 {chegirma_miqdori}\n"
        text += "📅 <b>Muddati:</b> "
        if chegirma["ended_at"]:
            text += f"<b>{chegirma['ended_at'][:10]}</b>\n"
        else:
            text += "<b>Cheklovsiz!</b>\n"
        text += "➖➖➖➖➖➖➖➖\n"

    return text
