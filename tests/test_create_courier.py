import allure
import pytest
from urls import Urls
from helpers import generate_random_string
from api_client import create_courier, login_courier, delete_courier

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = generate_random_string()
        password = generate_random_string()
        payload = {
            "login": login,
            "password": password,
            "firstName": "Test"
        }
        
        response = create_courier(payload)
        
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
        assert response.json() == {"ok": True}
        

        login_payload = {"login": login, "password": password}
        response_login = login_courier(login_payload)
        courier_id = response_login.json().get("id")
        
        # Убрала if
        assert courier_id is not None, "Не удалось получить ID созданного курьера"
        delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier):
        login, password = courier
        payload = {
            "login": login,
            "password": password,
            "firstName": "Test"
        }
        
        response = create_courier(payload)
        
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
        
        response = create_courier(payload)
        
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        assert "Недостаточно данных для создания учетной записи" in response.text