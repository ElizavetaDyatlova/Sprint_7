import allure
import requests
from urls import Urls

@allure.feature("Список заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_success(self):
        response = requests.get(Urls.GET_ORDERS_LIST)
        
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        
        response_json = response.json()
        assert "orders" in response_json, "В ответе отсутствует ключ 'orders'"
        assert isinstance(response_json["orders"], list), "Поле 'orders' не является списком"