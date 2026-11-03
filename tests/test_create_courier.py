import allure
import pytest
import requests
import random
import string
from urls import Urls
from helpers import get_courier_id, delete_courier


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        password = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        
        payload = {
            "login": login,
            "password": password,
            "firstName": "Test"
        }
        
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        assert response.json() == {"ok": True}
        
        courier_id = get_courier_id(login, password)
        if courier_id:
            delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1],
            "firstName": courier[2]
        }
        
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    @allure.title("Ошибка при создании курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_error(self, missing_field):
        payload = {
            "login": "some_login",
            "password": "some_password",
            "firstName": "Test"
        }
        del payload[missing_field]
        
        response = requests.post(Urls.CREATE_COURIER, data=payload)
        
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        assert "Недостаточно данных для создания учетной записи" in response.text