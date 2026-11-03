import allure
import pytest
import requests
from urls import Urls

ORDER_BASE_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-06-06",
    "comment": "Saske, come back to Konoha"
}

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета: {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_success(self, color):
        payload = ORDER_BASE_PAYLOAD.copy()
        payload["color"] = color
        
        response = requests.post(Urls.CREATE_ORDER, json=payload)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        response_json = response.json()
        assert "track" in response_json, "В ответе отсутствует ключ 'track'"