import requests
import random
import string
from urls import Urls

def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(Urls.LOGIN_COURIER, data=payload)
    return response.json().get("id")

def delete_courier(courier_id):
    response = requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")
    return response