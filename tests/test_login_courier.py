import allure
import pytest
import requests
from urls import Urls


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }
        
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        
        assert response.status_code == 200

        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при авторизации с неверным паролем")
    def test_login_courier_wrong_password_error(self, courier):
        payload = {
            "login": courier[0],
            "password": "wrong_password_123"
        }
        
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_non_existent_user_error(self):
        payload = {
            "login": "non_existent_login_999",
            "password": "some_password"
        }
        
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Ошибка при авторизации без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field_error(self, courier, missing_field):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        del payload[missing_field]
        
        response = requests.post(Urls.LOGIN_COURIER, data=payload)
        
        assert response.status_code == 400, f"Баг стенда! Ожидался 400, получен {response.status_code}"
        assert "Недостаточно данных для входа" in response.text