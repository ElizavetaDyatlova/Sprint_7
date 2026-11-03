import allure
import pytest
from api_client import login_courier

@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier):
        login, password = courier
        payload = {"login": login, "password": password}
        
        response = login_courier(payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при авторизации с неверным паролем")
    def test_login_courier_wrong_password_error(self, courier):
        login, _ = courier
        payload = {"login": login, "password": "wrong_password_123"}
        
        response = login_courier(payload)
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_non_existent_user_error(self):
        payload = {"login": "non_existent_login_999", "password": "some_password"}
        
        response = login_courier(payload)
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Ошибка при авторизации без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field_error(self, courier, missing_field):
        login, password = courier
        payload = {"login": login, "password": password}
        del payload[missing_field]
        
        response = login_courier(payload)
        
        assert response.status_code == 400, f"Баг стенда. Ожидался 400, получен {response.status_code}"
        assert "Недостаточно данных для входа" in response.text