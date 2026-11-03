import allure
import pytest
from data import ORDER_BASE_PAYLOAD
from api_client import create_order

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета: {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_success(self, color):
        payload = ORDER_BASE_PAYLOAD.copy()
        payload["color"] = color
        
        response = create_order(payload)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует ключ 'track'"